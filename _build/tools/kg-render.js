/* 知识图谱渲染：本地 vis-network，无 CDN 依赖。
   桌面：固定分栏布局（章节在左、概念在右），不用力导向，避免节点挤成一团。
   窄屏（<620px）：按章节顺序的路线图，避免缩得太小。
   KG.init(container, manifest, {hashPrefix}) */
(function(){
  function esc(s){
    return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];
    });
  }
  function chNum(ch, i){
    var m = String(ch.title || '').match(/第\s*(\d+)\s*章/);
    return m ? m[1] : String(i + 1);
  }
  function shortTitle(ch){
    return String(ch.title || ch.id).replace(/^第\s*\d+\s*章[：:]\s*/, '').replace(/^第\s*\d+\s*章\s*/, '');
  }
  function clip(s, n){
    s = String(s || '');
    return s.length > n ? s.slice(0, n) + '…' : s;
  }
  function fitNet(net){
    try{
      net.fit({animation:false});
      if(net.getScale() > 1.12){
        net.moveTo({position: net.getViewPosition(), scale: 1.12, animation:false});
      }
    }catch(e){}
  }

  function renderList(container, chapters, concepts, opts, status){
    var prefix = opts.hashPrefix || '#/';
    var chaptersById = {};
    chapters.forEach(function(ch, i){ chaptersById[ch.id] = {ch: ch, i: i}; });
    var used = {};
    var html = ['<div class="kg-list">'];
    chapters.forEach(function(ch, i){
      var pre = (ch.prerequisites || []).map(function(p){
        var pid = typeof p === 'string' ? p : (p && p.id);
        var hit = chaptersById[pid];
        return hit ? '<a href="' + prefix + 'chapter/' + pid + '">第' + chNum(hit.ch, hit.i) + '章</a>' : esc(pid);
      }).filter(Boolean);
      var chips = [];
      concepts.forEach(function(c){
        if(used[c.id]) return;
        if((c.chapterIds || []).indexOf(ch.id) >= 0){
          used[c.id] = true;
          chips.push('<a class="kg-chip" href="' + prefix + 'concept/' + c.id + '">' + esc(c.title || c.id) + '</a>');
        }
      });
      html.push('<div class="kg-item">');
      html.push('<a class="kg-chapter" href="' + prefix + 'chapter/' + ch.id + '">' +
                '<span class="kg-num">第' + chNum(ch, i) + '章</span> ' + esc(shortTitle(ch)) + '</a>');
      html.push('<div class="kg-pre">前置：' + (pre.length ? pre.join('、') : '无') + '</div>');
      if(chips.length) html.push('<div class="kg-chips"><span class="kg-chip-label">概念</span>' + chips.join('') + '</div>');
      html.push('</div>');
    });
    var leftovers = concepts.filter(function(c){ return !used[c.id]; });
    if(leftovers.length){
      html.push('<div class="kg-item"><div class="kg-chapter">其他概念</div><div class="kg-chips">' +
                leftovers.map(function(c){ return '<a class="kg-chip" href="' + prefix + 'concept/' + c.id + '">' + esc(c.title || c.id) + '</a>'; }).join('') +
                '</div></div>');
    }
    html.push('</div>');
    container.innerHTML = html.join('');
    container.classList.add('kg-list-mode');
    container.dataset.kgMode = 'list';
    if(status) status.textContent = '手机窄屏模式：按学习顺序列章节，点章节或概念直接跳转。横屏或桌面端会显示关系图。';
  }

  function init(container, manifest, opts){
    opts = opts || {};
    var status = document.getElementById('graph-status');
    try{
      if(window.__kgNet && window.__kgNet.destroy){ try{ window.__kgNet.destroy(); }catch(e){} }
      window.__kgNet = null;
      container.classList.remove('kg-list-mode');
      container.innerHTML = '';
      manifest = manifest || {};
      var chapters = manifest.chapters || [];
      var concepts = manifest.concepts || [];
      if(!chapters.length && !concepts.length){
        if(status) status.textContent = '这本书还没有可画的节点。';
        return;
      }
      var narrow = container.clientWidth > 0 && container.clientWidth < 620;
      if(narrow){
        renderList(container, chapters, concepts, opts, status);
        container.__kgArgs = {manifest: manifest, opts: opts};
        return;
      }
      if(!window.vis || !vis.Network){
        if(status) status.textContent = '图谱组件未加载，请刷新页面。';
        return;
      }

      var CH_X = 260, C_X = 720, TOP = 40, SPAN = 600;
      var chY = function(i){
        return chapters.length <= 1 ? 340 : TOP + i * SPAN / (chapters.length - 1);
      };
      var cY = function(j){
        return concepts.length <= 1 ? 340 : TOP + j * SPAN / (concepts.length - 1);
      };
      if(!concepts.length){ CH_X = 470; }

      var nodes = [], edges = [], chapterIds = {};
      chapters.forEach(function(ch, i){
        chapterIds[ch.id] = true;
        nodes.push({
          id: 'ch_' + ch.id,
          label: '第' + chNum(ch, i) + '章 ' + clip(shortTitle(ch), 12),
          title: String(ch.title || ch.id),
          x: CH_X, y: chY(i),
          shape: 'box',
          color: {background:'#dbeafe', border:'#3b82f6', highlight:{background:'#bfdbfe', border:'#2563eb'}},
          font: {size: 12, color: '#1e3a8a', face: 'PingFang SC, Microsoft YaHei, sans-serif'},
          margin: {top: 8, bottom: 8, left: 10, right: 10},
          widthConstraint: {maximum: 220},
          borderWidth: 1
        });
      });
      concepts.forEach(function(c, j){
        nodes.push({
          id: 'c_' + c.id,
          label: clip(c.title || c.id, 12),
          title: String(c.title || c.id) + '（点击查看概念页）',
          x: C_X, y: cY(j),
          shape: 'box',
          color: {background:'#fef3c7', border:'#d97706', highlight:{background:'#fde68a', border:'#b45309'}},
          font: {size: 12, color: '#78350f', face: 'PingFang SC, Microsoft YaHei, sans-serif'},
          margin: {top: 7, bottom: 7, left: 10, right: 10},
          widthConstraint: {maximum: 220},
          borderWidth: 1
        });
      });
      var ids = {};
      nodes.forEach(function(n){ ids[n.id] = true; });
      function addEdge(from, to, style){
        if(!ids[from] || !ids[to]) return;
        edges.push({
          from: from, to: to,
          arrows: {to: {enabled: style.arrow !== false, scaleFactor: 0.6}},
          color: {color: style.color, highlight: style.color},
          width: style.width || 1.3,
          dashes: style.dashes || false,
          smooth: {enabled: true, type: 'continuous', roundness: 0.2}
        });
      }
      chapters.forEach(function(ch){
        (ch.prerequisites || []).forEach(function(p){
          var pid = typeof p === 'string' ? p : (p && p.id);
          if(chapterIds[pid]) addEdge('ch_' + pid, 'ch_' + ch.id, {color:'#94a3b8', width:1.5});
        });
      });
      concepts.forEach(function(c){
        var hasPrereq = false;
        (c.prerequisites || []).forEach(function(p){
          var pid = typeof p === 'string' ? p : (p && p.id);
          var ptype = typeof p === 'string' ? 'hard' : ((p && p.type) || 'hard');
          var from = (String(pid).indexOf('ch') === 0 && chapterIds[pid]) ? 'ch_' + pid : 'c_' + pid;
          if(!ids[from]) return;
          hasPrereq = true;
          if(ptype === 'hard') addEdge(from, 'c_' + c.id, {color:'#dc2626', width:1.8});
          else if(ptype === 'soft') addEdge(from, 'c_' + c.id, {color:'#9ca3af', width:1.2, dashes:[5,4]});
          else addEdge(from, 'c_' + c.id, {color:'#3b82f6', width:1.2, dashes:[5,4]});
        });
        if(!hasPrereq && c.chapterIds && c.chapterIds.length && chapterIds[c.chapterIds[0]]){
          addEdge('ch_' + c.chapterIds[0], 'c_' + c.id, {color:'#cbd5e1', width:1, dashes:[4,4], arrow:false});
        }
      });

      var options = {
        autoResize: true,
        height: '100%',
        width: '100%',
        nodes: {shape:'box', borderWidth:1, shadow:false},
        edges: {smooth:{enabled:true, type:'continuous', roundness:0.2}, selectionWidth:1.5},
        layout: {improvedLayout: false},
        physics: {enabled: false},
        interaction: {hover:true, tooltipDelay:120, zoomView:true, dragView:true, dragNodes:true, multiselect:false}
      };
      var data = {nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges)};
      var net = new vis.Network(container, data, options);
      window.__kgNet = net;
      container.dataset.kgMode = 'graph';
      container.__kgArgs = {manifest: manifest, opts: opts};
      if(status) status.textContent = concepts.length
        ? '共 ' + nodes.length + ' 个节点、' + edges.length + ' 条关系。左侧章节按学习顺序自上而下，右侧是概念；滚轮缩放，点击跳转。'
        : '共 ' + nodes.length + ' 个节点、' + edges.length + ' 条关系。章节按学习顺序自上而下；滚轮缩放，点击跳转。';
      net.on('click', function(params){
        if(!params.nodes || !params.nodes.length) return;
        var nid = params.nodes[0];
        var target = nid.indexOf('c_') === 0 ? ('concept/' + nid.slice(2)) : ('chapter/' + nid.slice(3));
        location.hash = (opts.hashPrefix || '#/') + target;
      });
      setTimeout(function(){ if(window.__kgNet === net) fitNet(net); }, 60);
      setTimeout(function(){ if(window.__kgNet === net) fitNet(net); }, 360);
    }catch(err){
      if(status) status.textContent = '图谱渲染失败：' + (err && err.message ? err.message : err);
      if(window.console && console.error) console.error(err);
    }
  }

  window.KG = {
    init: init,
    fit: function(){ if(window.__kgNet) fitNet(window.__kgNet); }
  };
  if(!window.__kgResizeBound){
    window.__kgResizeBound = true;
    var timer = null;
    window.addEventListener('resize', function(){
      clearTimeout(timer);
      timer = setTimeout(function(){
        var c = document.getElementById('graph-container');
        if(!c) return;
        var want = c.clientWidth > 0 && c.clientWidth < 620 ? 'list' : 'graph';
        if(c.dataset.kgMode && c.dataset.kgMode !== want && c.__kgArgs){
          init(c, c.__kgArgs.manifest, c.__kgArgs.opts);
        } else if(window.__kgNet){ fitNet(window.__kgNet); }
      }, 220);
    });
  }
})();
