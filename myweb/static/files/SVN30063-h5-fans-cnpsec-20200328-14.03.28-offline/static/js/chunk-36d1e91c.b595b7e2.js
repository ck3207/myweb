(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-36d1e91c"],{"334e":function(e,t,i){i.r(t);var a=function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{staticClass:"page-container"},[i("van-pull-refresh",{directives:[{name:"scroll-maintain",rawName:"v-scroll-maintain"}],staticClass:"pull-refresh-box page-content",on:{refresh:e.onRefresh},model:{value:e.isPullRefreshLoading,callback:function(t){e.isPullRefreshLoading=t},expression:"isPullRefreshLoading"}},[i("LoadMore",{ref:"myLoadMore",attrs:{bottomMethod:e.loadBottom,canInif:e.canInif,isFinal:e.isFinal}},[e._l(e.viewList,(function(e,t){return i("ViewCard",{key:t,attrs:{viewData:e,componentType:"purchasedViews"}})})),i("NoData",{directives:[{name:"show",rawName:"v-show",value:e.showNoData,expression:"showNoData"}]}),e.isFinal&&!e.showNoData?i("div",{staticClass:"reach-bottom"},[e._v("已经到底了")]):e._e()],2)],1)],1)},n=[],s=(i("96cf"),i("3b8d")),r=(i("7f7f"),i("d225")),o=i("b0b4"),c=i("308d"),u=i("6bb5"),l=i("4e2b"),f=i("9ab4"),h=i("60a3"),d=i("1fee"),b=i("a2c9"),p=i("501e"),v=i("4bb5"),w=i("de0d"),m=function(e){function t(){var e;return Object(r["a"])(this,t),e=Object(c["a"])(this,Object(u["a"])(t).apply(this,arguments)),e.requestNum=20,e.isFinal=!1,e.canInif=!0,e.viewList=[],e.pageNo=1,e.showNoData=!1,e}return Object(l["a"])(t,e),Object(o["a"])(t,[{key:"beforeRouteEnter",value:function(e,t,i){i((function(e){"viewDetail"!==t.name&&(e.resetListData(),e.init())}))}},{key:"activated",value:function(){this.$forceUpdate()}},{key:"beforeRouteLeave",value:function(e,t,i){"viewDetail"!==e.name&&this.resetListData(),i()}},{key:"init",value:function(){var e=this;this.getViewList().then((function(t){if(!t.data_list.length)return e.showNoData=!0,e.isFinal=!0,void(e.canInif=!1);e.viewList=t.data_list,e.buildListData(t.data_list)}))}},{key:"pullRefreshInit",value:function(){var e=Object(s["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:this.resetListData(),this.init();case 2:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}()},{key:"buildListData",value:function(e){this.pageNo=this.pageNo+1,e.length<this.requestNum&&(this.isFinal=!0,this.canInif=!1)}},{key:"resetListData",value:function(){this.viewList=[],this.showNoData=!1,this.canInif=!0,this.isFinal=!1,this.pageNo=1}},{key:"getViewList",value:function(){return this.$services.getPurchasedViewpointList({data:{page_no:this.pageNo,page_size:this.requestNum}}).then((function(e){return e})).catch((function(e){console.log("getViewList error: ",e)}))}},{key:"loadBottom",value:function(){var e=this;setTimeout((function(){e.getViewList().then((function(t){e.viewList=e.viewList.concat(t.data_list),e.buildListData(t.data_list)}))}),200)}}]),t}(h["c"]);Object(f["a"])([v["a"]],m.prototype,"userInfo",void 0),m=Object(f["a"])([Object(h["a"])({components:{ViewCard:d["a"],LoadMore:b["a"],NoData:p["a"]},mixins:[w["a"]]})],m);var g=m,L=g,y=(i("bd60"),i("2877")),R=Object(y["a"])(L,a,n,!1,null,"2c8102d5",null);t["default"]=R.exports},"428d":function(e,t,i){},bd60:function(e,t,i){var a=i("428d"),n=i.n(a);n.a},d82a:function(e,t,i){e.exports=i.p+"static/img/failure.9971aa1e.png"},de0d:function(e,t,i){i("96cf");var a=i("3b8d"),n=i("d225"),s=i("b0b4"),r=i("308d"),o=i("6bb5"),c=i("4e2b"),u=i("9ab4"),l=i("60a3"),f=i("b3af"),h=function(e){function t(){var e;return Object(n["a"])(this,t),e=Object(r["a"])(this,Object(o["a"])(t).apply(this,arguments)),e.isPullRefreshLoading=!1,e.pullRefreshInitTimerId=null,e}return Object(c["a"])(t,e),Object(s["a"])(t,[{key:"deactivated",value:function(){this.isPullRefreshLoading=!1,this.pullRefreshInitTimerId=null,this.$notify.clear(),clearInterval(this.pullRefreshInitTimerId)}},{key:"onRefresh",value:function(){var e=this;this.pullRefreshInitTimerId=setTimeout(Object(a["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.pullRefreshInit();case 2:e.isPullRefreshLoading=!1,e.$notify({message:"数据加载成功",color:"#fff",background:"rgba(0,0,0,.5)"});case 4:case"end":return t.stop()}}),t)}))),f["e"])}}]),t}(l["c"]);h=Object(u["a"])([l["a"]],h),t["a"]=h},f6ab:function(e,t,i){e.exports=i.p+"static/img/bg_no_data.93c56ab0.png"}}]);