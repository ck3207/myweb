(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7f0d088e"],{"8b83":function(t,a,s){var i=s("abf7"),e=s.n(i);e.a},abf7:function(t,a,s){},c04e:function(t,a,s){s.r(a);var i=function(){var t=this,a=t.$createElement,s=t._self._c||a;return s("div",{staticClass:"page-content"},[s("div",{staticClass:"follow-stock-pool"},[s("div",{staticClass:"stock-pool"},[s("div",{staticClass:"adviser-group"},[s("img",{attrs:{src:"brokerInfo.broker_avatar | formatImagePath"},on:{error:t.shopAvatarError}}),s("span",{staticClass:"title"},[t._v(t._s(t.broker_name))]),s("span",{staticClass:"dec"},[t._v(t._s(t.identy_type))])]),s("div",{staticClass:"tag-list"},[s("span",[t._v("恒生电子")]),s("span",[t._v("恒生电子")]),s("span",[t._v("恒生电子")]),s("router-link",{attrs:{to:"adviserList"}},[t._v("......")])],1)]),s("div",{staticClass:"stock-pool"},[s("div",{staticClass:"adviser-group"},[s("img",{attrs:{src:"brokerInfo.broker_avatar | formatImagePath"},on:{error:t.shopAvatarError}}),s("span",{staticClass:"title"},[t._v(t._s(t.broker_name))]),s("span",{staticClass:"dec"},[t._v(t._s(t.identy_type))])]),s("div",{staticClass:"tag-list"},[s("span",[t._v("恒生电子")]),s("span",[t._v("恒生电子")]),s("span",[t._v("恒生电子")]),s("router-link",{attrs:{to:"adviserList"}},[t._v("......")])],1)])])])},e=[],r=s("d225"),n=s("b0b4"),o=s("308d"),c=s("6bb5"),l=s("4e2b"),d=s("9ab4"),p=s("60a3"),v=s("a2c9"),u=s("501e"),_=function(t){function a(){var t;return Object(r["a"])(this,a),t=Object(o["a"])(this,Object(c["a"])(a).apply(this,arguments)),t.pageNo=1,t.pageSize=15,t.orderList=[],t.showNoData=!1,t.canInif=!1,t.isFinal=!1,t}return Object(l["a"])(a,t),Object(n["a"])(a,[{key:"activated",value:function(){this.orderList=[],this.showNoData=!1,this.canInif=!1,this.isFinal=!1,this.pageNo=0,setTimeout((function(){}),200)}},{key:"getOrderList",value:function(){var t=this,a={order_type:"0",page_no:this.pageNo,page_size:this.pageSize};return this.$services.funcOrderManage({data:a}).then((function(a){if(!a.data_list.length)return t.showNoData=!0,t.isFinal=!0,void(t.canInif=!1);t.orderList=a.data_list,t.buildListData(a.data_list)}))}},{key:"buildListData",value:function(t){this.pageNo++,t.length<this.pageSize&&(this.isFinal=!0,this.canInif=!1)}},{key:"loadBottom",value:function(){var t=this;this.getOrderList().then((function(a){t.orderList=t.orderList.concat(a.data_list),t.buildListData(a.data_list)}))}}]),a}(p["c"]);_=Object(d["a"])([Object(p["a"])({components:{LoadMore:v["a"],NoData:u["a"]}})],_);var b=_,h=b,f=(s("8b83"),s("2877")),g=Object(f["a"])(h,i,e,!1,null,"8780416a",null);a["default"]=g.exports},f6ab:function(t,a,s){t.exports=s.p+"static/img/bg_no_data.93c56ab0.png"}}]);