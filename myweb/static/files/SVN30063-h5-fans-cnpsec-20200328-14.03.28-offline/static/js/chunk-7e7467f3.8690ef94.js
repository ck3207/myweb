(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7e7467f3"],{"6dc5":function(t,s,i){},"7a7f":function(t,s,i){i.r(s);var a=function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"stock-pool-container"},[i("div",{staticClass:"stock-pool-tool-bar"},[i("div",{staticClass:"stock-pool-tabs"},[i("span",{class:{active:0===t.currentTabIndex},on:{click:function(s){return t.handleClickTab(0)}}},[t._v("当前持仓")]),i("span",{class:{active:1===t.currentTabIndex},on:{click:function(s){return t.handleClickTab(1)}}},[t._v("历史调仓")])]),i("div",{directives:[{name:"show",rawName:"v-show",value:1!=t.followType,expression:"followType != 1"}],staticClass:"flow-adviser-tips"},[t._v("关注投顾，唤醒股票池")])]),i("div",{directives:[{name:"show",rawName:"v-show",value:0===t.currentTabIndex,expression:"currentTabIndex === 0"}],staticClass:"current-position"},[t._m(0),t.positionList.length?i("div",{staticClass:"stock-list"},t._l(t.positionList,(function(s,a){return i("div",{key:a,staticClass:"stock-list-item"},[i("div",{staticClass:"stock-list-content"},[1==t.followType?i("span",{staticClass:"stock-name",on:{click:function(i){return t.textStockClick(s.stock_code,s.stock_name)}}},[i("b",[t._v(t._s(s.stock_name))]),i("em",[t._v(t._s(s.stock_code))])]):i("span",{staticClass:"stock-name"},[i("b",[t._v(t._s(t.collectHide(s.stock_name)))]),i("em",[t._v(t._s(t.collectHide(s.stock_code)))])]),i("span",{staticClass:"stock-rate",class:[s.rate<0?"down":"up"]},[t._v(t._s((100*s.rate).toFixed(2))+"%")]),i("span",{staticClass:"stock-price"},[i("b",[t._v(t._s(t._f("formatNumber")(s.last_price,2)))]),i("em",[t._v(t._s(t._f("formatNumber")(s.price,2)))])]),i("span",{staticClass:"stock-time"},[t._v(t._s(s.days)+"天")])]),i("div",{staticClass:"stock-item-time-info"},[i("span",[t._v("入选时间")]),i("span",[t._v(t._s(s.create_time))])])])})),0):t._e(),i("NoData",{directives:[{name:"show",rawName:"v-show",value:t.showNoPosition,expression:"showNoPosition"}]}),t.showNoPosition?t._e():i("div",{staticClass:"reach-bottom"},[t._v("已经到底了")])],1),i("div",{directives:[{name:"show",rawName:"v-show",value:1===t.currentTabIndex,expression:"currentTabIndex === 1"}],staticClass:"history-adjust"},[i("LoadMore",{attrs:{bottomMethod:t.loadBottom,canInif:t.canInif,isFinal:t.isFinal}},[t.transactionList.length?i("Adjust",{attrs:{followType:t.followType,transactionList:t.transactionList},on:{"update:followType":function(s){t.followType=s},"update:follow-type":function(s){t.followType=s}}}):t._e(),i("NoData",{directives:[{name:"show",rawName:"v-show",value:t.showNoTransactionData,expression:"showNoTransactionData"}]}),t.isFinal&&!t.showNoTransactionData?i("div",{staticClass:"reach-bottom"},[t._v("已经到底了")]):t._e()],1)],1)])},o=[function(){var t=this,s=t.$createElement,i=t._self._c||s;return i("div",{staticClass:"stock-list-header"},[i("span",{staticClass:"stock-name"},[t._v("名称/代码")]),i("span",{staticClass:"stock-rate"},[t._v("入选后涨幅")]),i("span",{staticClass:"stock-price"},[t._v("最新/入选价格")]),i("span",{staticClass:"stock-time"},[t._v("信号持续")])])}],e=(i("ac6a"),i("a481"),i("d225")),n=i("b0b4"),c=i("308d"),r=i("6bb5"),l=i("4e2b"),h=i("9ab4"),u=i("60a3"),p=i("253a"),d=i("501e"),v=i("5c3a"),_=i("a2c9"),f=i("4bb5"),k=i("d257"),b=function(t){function s(){var t;return Object(e["a"])(this,s),t=Object(c["a"])(this,Object(r["a"])(s).apply(this,arguments)),t.currentTabIndex=0,t.showNoTransactionData=!1,t.showNoPosition=!1,t.positionList=[],t.transactionList=[],t.canInif=!1,t.isFinal=!1,t.pageSize=30,t.pageNo=1,t}return Object(l["a"])(s,t),Object(n["a"])(s,[{key:"activated",value:function(){this.isLogin&&(this.resetData(),this.getPositionStock(),this.getTransactionList())}},{key:"resetData",value:function(){this.showNoPosition=!1,this.positionList=[],this.showNoPosition=!1,this.showNoTransactionData=!1,this.transactionList=[],this.canInif=!1,this.isFinal=!1,this.pageNo=1}},{key:"collectHide",value:function(t){var s=t+"";return s.replace(/\S/g,"*")}},{key:"getPositionStock",value:function(){var t=this,s={broker_id:this.$route.query.brokerId,page_no:this.pageNo,page_size:this.pageSize+100,status:"0"};this.$services.qryBrokerStockPool({data:s}).then((function(s){t.filterStockList(s.data_list)})).catch((function(t){console.error(t)}))}},{key:"filterStockList",value:function(t){t.length?(this.showNoPosition=!1,this.positionList=t):(this.positionList=[],this.showNoPosition=!0)}},{key:"getTransactionList",value:function(t){var s=this,i={broker_id:this.$route.query.brokerId,page_no:this.pageNo,page_size:this.pageSize};this.$services.qryBrokerStockPool({data:i}).then((function(i){var a=i.data_list||[];Array.isArray(a)&&a.forEach((function(t){t.init_date=t.create_time,t.entrust_bs=t.flag+""==="1"?"0":"1",t.entrust_reason=t.remark,t.isShowDetail=!0,t.business_price=t.last_price,t.prod_code=t.stock_code,t.prod_name=t.stock_name})),console.log("result",a),s.filterPositionList(a,t)})).catch((function(t){console.log("getPositionList",t)}))}},{key:"filterPositionList",value:function(t,s){t.length?(t.length>=this.pageSize?(this.canInif=!0,this.isFinal=!1):(this.canInif=!1,this.isFinal=!0),this.transactionList=s?this.transactionList.concat(t):t):(this.canInif=!1,this.isFinal=!0,s||(this.showNoTransactionData=!0))}},{key:"loadBottom",value:function(){var t=this;setTimeout((function(){t.getTransactionList("append")}),200)}},{key:"handleClickTab",value:function(t){this.currentTabIndex!==t&&(this.currentTabIndex=t,this.resetData(),0===t?this.getPositionStock():this.getTransactionList())}},{key:"textStockClick",value:function(t,s){Object(k["q"])(t,s)}}]),s}(u["c"]);Object(h["a"])([Object(u["b"])({type:String})],b.prototype,"adviserId",void 0),Object(h["a"])([Object(u["b"])({type:String})],b.prototype,"followType",void 0),Object(h["a"])([f["a"]],b.prototype,"userInfo",void 0),Object(h["a"])([f["a"]],b.prototype,"isLogin",void 0),b=Object(h["a"])([Object(u["a"])({components:{Adjust:p["a"],NoData:d["a"],Spinner:v["a"],LoadMore:_["a"]}})],b);var w=b,m=w,g=(i("c154"),i("2877")),y=Object(g["a"])(m,a,o,!1,null,"af7bc358",null);s["default"]=y.exports},c154:function(t,s,i){var a=i("6dc5"),o=i.n(a);o.a},f6ab:function(t,s,i){t.exports=i.p+"static/img/bg_no_data.93c56ab0.png"}}]);