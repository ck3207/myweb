(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-91040a44"],{"05cc":function(t,e,a){},"0760":function(t,e,a){var i=a("05cc"),s=a.n(i);s.a},1750:function(t,e,a){a("7f7f");var i=a("d257");e["a"]={mounted:function(){var t=this;Object(i["l"])((function(){t.$store.dispatch("getDataFromNative").then((function(e){console.log("唤起壳子登录之后的回调函数执行，返回 mobile",e),e&&"null"!==e&&(t.$store.dispatch("userLogin",{mobile:e}),t.init())}))}))},activated:function(){var t=this.$route.name;"liveList"!==t&&"adviserList"!==t&&this.init()}}},"1c2f":function(t,e,a){var i=a("6a3d"),s=a.n(i);s.a},"24e3":function(t,e,a){var i=a("2585"),s=a.n(i);s.a},2585:function(t,e,a){},"2a27":function(t,e,a){a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"page-container"},[a("van-pull-refresh",{directives:[{name:"scroll-maintain",rawName:"v-scroll-maintain"}],staticClass:"pull-refresh-box page-content",on:{refresh:t.onRefresh},model:{value:t.isPullRefreshLoading,callback:function(e){t.isPullRefreshLoading=e},expression:"isPullRefreshLoading"}},[a("Search",{staticClass:"adviser-search",attrs:{historyList:t.historyList,searchFunc:t.searchAdviser,searchResult:t.searchAdviserResult},on:{clearHistory:t.handleClearHistory},scopedSlots:t._u([{key:"search-result",fn:function(e){var i=e.resultItem;return[a("div",{staticClass:"search-result-item",on:{click:function(e){return t.handleClickAdviserCard(i)}}},[t._v(t._s(i.broker_name))])]}}])}),a("CommonTab",{staticClass:"adviser-tab",attrs:{tabList:t.adviserTabList},model:{value:t.tabKey,callback:function(e){t.tabKey=e},expression:"tabKey"}}),a("LoadMore",{ref:"myLoadMore",attrs:{bottomMethod:t.loadBottom,canInif:t.canInif,isFinal:t.isFinal}},[t._l(t.adviserList,(function(e,i){return a("AdviserCard",{key:i,attrs:{incomeType:t.tabKey,adviserData:e}})})),a("NoData",{directives:[{name:"show",rawName:"v-show",value:t.showNoData,expression:"showNoData"}]}),t.isFinal&&!t.showNoData?a("div",{staticClass:"reach-bottom"},[t._v("已经到底了")]):t._e()],2)],1)],1)},s=[],n=(a("96cf"),a("3b8d")),r=(a("7f7f"),a("d225")),o=a("b0b4"),c=a("308d"),l=a("6bb5"),u=a("4e2b"),d=a("9ab4"),v=a("60a3"),f=a("4bb5"),h=a("1750"),p=a("500f"),b=a("9d59"),m=a("26b9"),y=a("b804"),k=a("a2c9"),_=a("501e"),g=a("de0d"),L=function(t){function e(){var t;return Object(r["a"])(this,e),t=Object(c["a"])(this,Object(l["a"])(e).apply(this,arguments)),t.adviserTabList=[{name:"人气",key:"7"},{name:"总收益",key:"0"},{name:"年收益",key:"4"},{name:"月收益",key:"3"},{name:"周收益",key:"2"}],t.tabKey="7",t.pageSize=20,t.showNoData=!1,t.isFinal=!1,t.canInif=!0,t.positionStr=0,t.adviserList=[],t.tabContent="人气",t.historyList=[],t.searchAdviserResult=[],t}return Object(u["a"])(e,t),Object(o["a"])(e,[{key:"onTabIndexChange",value:function(){this.resetListData(),this.getAdviserList()}},{key:"beforeRouteEnter",value:function(t,e,a){a((function(t){"adviserDetail"!==e.name&&setTimeout((function(){t.init()}),300)}))}},{key:"activated",value:function(){this.$forceUpdate()}},{key:"beforeRouteLeave",value:function(t,e,a){"adviserDetail"!==t.name&&(this.resetListData(),this.tabKey="7"),a()}},{key:"init",value:function(){this.resetListData(),this.getAdviserList()}},{key:"pullRefreshInit",value:function(){var t=Object(n["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:this.positionStr=0,this.getAdviserList();case 2:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},{key:"getAdviserList",value:function(t){var e=this,a={tenant_key:window.LOCAL_CONFIG.TENANT_KEY,request_num:this.pageSize,position_str:this.positionStr,follow_type:0,extend_type:0,tenant_id:this.userInfo.tenant_id,customer_id:this.userInfo.customer_id||0,combination_sort_type:this.tabKey};this.$services.getAdviserList({data:a}).then((function(a){var i=a.data_list||[];e.filterList(i,t)})).catch((function(t){console.log("getAdviserList error: ",t)}))}},{key:"filterList",value:function(t,e){t.length?(this.positionStr=t[t.length-1].position_str,t.length>=this.pageSize?(this.canInif=!0,this.isFinal=!1):(this.canInif=!1,this.isFinal=!0),this.adviserList=e?this.adviserList.concat(t):t):(this.canInif=!1,this.isFinal=!0,e||(this.showNoData=!0))}},{key:"loadBottom",value:function(){var t=this;setTimeout((function(){t.getAdviserList("append")}),200)}},{key:"resetListData",value:function(){this.adviserList=[],this.showNoData=!1,this.canInif=!0,this.isFinal=!1,this.positionStr=0}},{key:"searchAdviser",value:function(t){var e=this;return this.searchAdviserResult=[],this.$services.getAdviserList({data:{tenant_key:window.LOCAL_CONFIG.TENANT_KEY,sort_type:this.tabKey,broker_name:t,request_num:this.pageSize,position_str:0,follow_type:0,tenant_id:this.userInfo.tenant_id}}).then((function(t){e.searchAdviserResult=t.data_list}))}},{key:"handleClearHistory",value:function(){this.historyList=[]}},{key:"handleClickAdviserCard",value:function(t){this.$router.push({path:"/adviserDetail",query:{brokerId:t.broker_id,brokerKey:t.broker_key}})}}]),e}(v["c"]);Object(d["a"])([f["a"]],L.prototype,"ltbToken",void 0),Object(d["a"])([f["a"]],L.prototype,"userInfo",void 0),Object(d["a"])([f["a"]],L.prototype,"isLogin",void 0),Object(d["a"])([Object(v["d"])("tabKey")],L.prototype,"onTabIndexChange",null),L=Object(d["a"])([Object(v["a"])({components:{AdviserCard:p["a"],Search:b["a"],CommonTab:m["a"],Sticky:y["a"],LoadMore:k["a"],NoData:_["a"]},mixins:[h["a"],g["a"]]})],L);var w=L,O=w,x=(a("0760"),a("2877")),D=Object(x["a"])(O,i,s,!1,null,"c19b6e04",null);e["default"]=D.exports},"500f":function(t,e,a){var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"adviser-card-container",on:{click:t.handleClickAdviserCard}},[a("div",{staticClass:"adviser-card-header"},[a("img",{attrs:{src:t._f("formatImagePath")(t.adviserData.manager_avatar),alt:t.adviserData.manager_avatar},on:{error:t.shopAvatarError}}),a("b",[t._v(t._s(t.adviserData.manager_name))]),t.adviserData.brokertag_name?a("span",t._l(t.formatBrokerTags(t.adviserData.brokertag_name),(function(e){return a("em",[t._v(t._s(e))])})),0):t._e()]),a("div",{staticClass:"adviser-branch-name"},[t._v(t._s(t.adviserData.branch_name))]),a("div",{staticClass:"adviser-info-group"},[a("div",{staticClass:"adviser-info-left"},[a("span",[a("strong",{class:{up:t.adviserData.income_ratio>0,down:t.adviserData.income_ratio<0}},[t._v("\n          "+t._s(t._f("parsePercentage")(t.adviserData.income_ratio,2))),a("i",[t._v("%")])]),a("em",[t._v(t._s(t.incomeTypeText))])]),a("span",[a("strong",{staticClass:"up"},[t._v(t._s(t.adviserData.follow_num)),a("i",[t._v("人")])]),a("em",[t._v("关注人数")])])]),a("div",{staticClass:"adviser-info-right"},[a("strong",{class:{ordered:1===+t.adviserData.follow_type},on:{click:function(e){return e.target!==e.currentTarget?null:(e.stopPropagation(),t.handleClickAdviserFollow(e))}}},[t._v("\n        "+t._s(1===+t.adviserData.follow_type?"已关注":"+关注")+"\n      ")])])])])},s=[],n=a("d225"),r=a("b0b4"),o=a("308d"),c=a("6bb5"),l=a("4e2b"),u=a("9ab4"),d=a("60a3"),v=a("4bb5"),f=a("d257"),h=function(t){function e(){return Object(n["a"])(this,e),Object(o["a"])(this,Object(c["a"])(e).apply(this,arguments))}return Object(l["a"])(e,t),Object(r["a"])(e,[{key:"handleClickAdviserCard",value:function(){this.$router.push({path:"/adviserDetail",query:{brokerId:this.adviserData.broker_id,brokerKey:this.adviserData.broker_key}})}},{key:"handleClickAdviserFollow",value:function(){var t=this;this.isLogin?1===+this.adviserData.follow_type?this.$services.setAdviserFollowCancel({data:{user_token:this.stuToken,access_token:this.accessToken,broker_id:this.adviserData.broker_id}}).then((function(e){"0"===e.error_no&&(t.adviserData.follow_type=2,t.adviserData.follow_num=+t.adviserData.follow_num-1)})):this.$services.setAdviserFollow({data:{user_token:this.stuToken,access_token:this.accessToken,broker_id:this.adviserData.broker_id}}).then((function(e){"0"===e.error_no&&(t.adviserData.follow_type=1,t.adviserData.follow_num=+t.adviserData.follow_num+1)})):this.$store.dispatch("nativeMobileLogin")}},{key:"formatBrokerTags",value:function(t){return Object(f["f"])(t)}},{key:"incomeTypeText",get:function(){var t={0:"总收益",7:"总收益",4:"年收益",3:"月收益",2:"周收益"};return t[this.incomeType]}}]),e}(d["c"]);Object(u["a"])([Object(d["b"])({type:Object,default:function(){return{}}})],h.prototype,"adviserData",void 0),Object(u["a"])([Object(d["b"])({type:String,default:function(){return"7"}})],h.prototype,"incomeType",void 0),Object(u["a"])([v["a"]],h.prototype,"isLogin",void 0),Object(u["a"])([v["a"]],h.prototype,"stuToken",void 0),Object(u["a"])([v["a"]],h.prototype,"accessToken",void 0),h=Object(u["a"])([d["a"]],h);var p=h,b=p,m=(a("24e3"),a("2877")),y=Object(m["a"])(b,i,s,!1,null,"62935ba3",null);e["a"]=y.exports},"6a3d":function(t,e,a){},b804:function(t,e,a){var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"vux-sticky-box"},[t._t("default")],2)},s=[];a("4917"),a("a481"),a("28a5");function n(t,e){if(t&&e){for(var a=e.split(" "),i=" "+t.className+" ",s=0,n=a.length;s<n;s++){var o=a[s];o&&(t.classList?t.classList.remove(o):r(t,o)&&(i=i.replace(" "+o+" "," ")))}t.classList||(t.className=trim(i))}}function r(t,e){if(!t||!e)return!1;if(-1!==e.indexOf(" "))throw new Error("className should not contain space.");return t.classList?t.classList.contains(e):(" "+t.className+" ").indexOf(" "+e+" ")>-1}function o(){var t=window.navigator.userAgent,e=t.match(/(iPad|iPhone|iPod)\s+OS\s([\d_.]+)/);return e&&e[2]&&parseInt(e[2].replace(/_/g,"."),10)>=6}function c(){for(var t=["","-webkit-","-ms-","-moz-","-o-"],e="",a=0;a<t.length;a++)e+="position:"+t[a]+"sticky";var i=document.createElement("div"),s=document.body;i.style.cssText="display:none"+e,s.appendChild(i);var n=/sticky/i.test(window.getComputedStyle(i).position);return s.removeChild(i),i=null,n}var l=function(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},a=e.scrollBox||window,i=e.offset||0,s=!0===e.checkStickySupport||!1;"string"===typeof a&&(a=document.getElementById(a));var r=t.offsetTop-i;a.removeEventListener("scroll",a.e);var l=function(){return a===window?document.documentElement&&document.documentElement.scrollTop||document.body.scrollTop:a.scrollTop},u=function(){var e=l();e>=r?(t.style.top=i+"px",t.classList.add("vux-fixed")):n(t,"vux-fixed")};s&&(o()||c())?(t.classList.add("vux-sticky"),t.style.top=i+"px"):(r=t.offsetTop-i,a.e=u,a.addEventListener("scroll",u))},u={name:"sticky",props:["scrollBox","offset","checkStickySupport"],mounted:function(){var t=this;this.$nextTick((function(){t.bindSticky()}))},activated:function(){this.removeFixed()},methods:{bindSticky:function(){var t=this;this.$nextTick((function(){l(t.$el,{scrollBox:t.scrollBox,offset:t.offset,checkStickySupport:"undefined"===typeof t.checkStickySupport||t.checkStickySupport})}))},removeFixed:function(){var t=document.querySelector(".vux-sticky-box");r(t,"vux-fixed")&&n(t,"vux-fixed")}}},d=u,v=(a("1c2f"),a("2877")),f=Object(v["a"])(d,i,s,!1,null,null,null);e["a"]=f.exports},de0d:function(t,e,a){a("96cf");var i=a("3b8d"),s=a("d225"),n=a("b0b4"),r=a("308d"),o=a("6bb5"),c=a("4e2b"),l=a("9ab4"),u=a("60a3"),d=a("b3af"),v=function(t){function e(){var t;return Object(s["a"])(this,e),t=Object(r["a"])(this,Object(o["a"])(e).apply(this,arguments)),t.isPullRefreshLoading=!1,t.pullRefreshInitTimerId=null,t}return Object(c["a"])(e,t),Object(n["a"])(e,[{key:"deactivated",value:function(){this.isPullRefreshLoading=!1,this.pullRefreshInitTimerId=null,this.$notify.clear(),clearInterval(this.pullRefreshInitTimerId)}},{key:"onRefresh",value:function(){var t=this;this.pullRefreshInitTimerId=setTimeout(Object(i["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,t.pullRefreshInit();case 2:t.isPullRefreshLoading=!1,t.$notify({message:"数据加载成功",color:"#fff",background:"rgba(0,0,0,.5)"});case 4:case"end":return e.stop()}}),e)}))),d["e"])}}]),e}(u["c"]);v=Object(l["a"])([u["a"]],v),e["a"]=v},f6ab:function(t,e,a){t.exports=a.p+"static/img/bg_no_data.93c56ab0.png"}}]);