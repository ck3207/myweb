(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6fcfea53"],{1826:function(t,e,i){i.r(e);var a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"view-list-container"},[i("div",{staticClass:"view-list-tab"},[i("span",{class:{active:0===t.currentTabIndex},on:{click:function(e){return t.handleClickTab(0)}}},[t._v("最新")]),i("span",{class:{active:1===t.currentTabIndex},on:{click:function(e){return t.handleClickTab(1)}}},[t._v("热门"),i("i",{staticClass:"hot"})])]),i("div",{staticClass:"view-list"},[i("LoadMore",{attrs:{bottomMethod:t.loadBottom,canInif:t.canInif,isFinal:!t.canInif}},[t._l(t.viewListData,(function(t){return i("ViewCard",{key:t.viewpoint_id,attrs:{viewData:t}})})),i("NoData",{directives:[{name:"show",rawName:"v-show",value:!t.loading&&t.noDataFlag,expression:"!loading && noDataFlag"}]}),i("div",{directives:[{name:"show",rawName:"v-show",value:!t.canInif&&!t.noDataFlag,expression:"!canInif && !noDataFlag"}],staticClass:"reach-bottom"},[t._v("已经到底了")])],2)],1)])},n=[],s=i("d225"),o=i("b0b4"),r=i("308d"),c=i("6bb5"),u=i("4e2b"),l=i("9ab4"),d=i("60a3"),v=i("1fee"),h=i("a2c9"),b=i("501e"),p=i("4bb5"),f=20,w=function(t){function e(){var t;return Object(s["a"])(this,e),t=Object(r["a"])(this,Object(c["a"])(e).apply(this,arguments)),t.currentTabIndex=0,t.viewListData=[],t.positionStr="0",t.canInif=!0,t.loading=!0,t}return Object(u["a"])(e,t),Object(o["a"])(e,[{key:"onSortTypeChange",value:function(){var t=this;this.resetList(),this.getViewList().then((function(e){t.viewListData=e,t.setListState(e)}))}},{key:"onAdviserIdChange",value:function(){var t=this;0===this.currentTabIndex?(this.resetList(),this.getViewList().then((function(e){t.viewListData=e,t.setListState(e)}))):this.currentTabIndex=0}},{key:"loadBottom",value:function(){var t=this;this.getViewList().then((function(e){t.viewListData=t.viewListData.concat(e),t.setListState(e)}))}},{key:"setListState",value:function(t){t.length>0&&(this.positionStr=t[t.length-1].position_str),t.length<f&&(this.canInif=!1)}},{key:"resetList",value:function(){this.positionStr="0",this.viewListData=[],this.canInif=!0}},{key:"getViewList",value:function(){var t=this;return this.loading=!0,this.$services.getAdviserViews({data:{tenant_key:window.LOCAL_CONFIG.TENANT_KEY,position_str:this.positionStr,viewpoint_status:"1",request_num:f,broker_id:this.adviserId,sort_type:this.sortType}}).then((function(e){return t.loading=!1,e.data_list})).catch((function(t){console.log("getViewList error: ",t)}))}},{key:"handleClickTab",value:function(t){this.currentTabIndex!==t&&(this.currentTabIndex=t)}},{key:"sortType",get:function(){var t={0:"3",1:"1"};return t[this.currentTabIndex]}},{key:"noDataFlag",get:function(){return 0===this.viewListData.length}}]),e}(d["c"]);Object(l["a"])([Object(d["b"])({type:String})],w.prototype,"adviserId",void 0),Object(l["a"])([p["a"]],w.prototype,"ltbToken",void 0),Object(l["a"])([Object(d["d"])("sortType")],w.prototype,"onSortTypeChange",null),Object(l["a"])([Object(d["d"])("adviserId")],w.prototype,"onAdviserIdChange",null),w=Object(l["a"])([Object(d["a"])({components:{ViewCard:v["a"],LoadMore:h["a"],NoData:b["a"]}})],w);var g=w,L=g,y=(i("b746"),i("2877")),I=Object(y["a"])(L,a,n,!1,null,"62077299",null);e["default"]=I.exports},5252:function(t,e,i){},b746:function(t,e,i){var a=i("5252"),n=i.n(a);n.a},d82a:function(t,e,i){t.exports=i.p+"static/img/failure.9971aa1e.png"},f6ab:function(t,e,i){t.exports=i.p+"static/img/bg_no_data.93c56ab0.png"}}]);