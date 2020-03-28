/**
 *
 * @authors liwb (you@example.org)
 * @date    2017/2/3 13:57
 * @version $ 根据不同环境配置对应的服务地址及变量，这里只放置必须要手动修改的变量
 */

/* name module */

window.LOCAL_CONFIG = {
  // 工作室服务及接口
  // API_HOME: 'http://10.20.37.226:80/',   // 测试
  API_HOME: 'http://10.20.34.83:8080/',   // 开发
  // 用户中心服务及接口
  // API_HSIAR: 'http://10.20.37.226/',  // 测试 
  API_HSIAR: 'http://10.20.34.83:8080/',   // 开发
  // 行情相关接口
  API_GTN: 'http://10.20.18.174:9018/',  // 测试
  // 客户信息管理，true：店铺模式，false：个人模式
  STORE_MODE: true,
  // 鲸腾iframe地址
  JINGTENG00: 'https://deindu5ky.lightyy.com/index.html', // 鲸腾：量化模型查询
  JINGTENG01: 'https://deindu5ky.lightyy.com/strategy_puton', // 鲸腾：量化模型上架审核
  JINGTENG02: 'https://deindu5ky.lightyy.com/strategy_pulloff', // 鲸腾：量化模型下架审核
  JINGTENG03: 'https://deindu5ky.lightyy.com/setup_model', // 鲸腾：选股过滤设置
  JINGTENG04: 'https://deindu5ky.lightyy.com/show_group', // 鲸腾：智能策略查询
  JINGTENG05: 'https://deindu5ky.lightyy.com/group_puton', // 鲸腾：智能策略上架审核
  JINGTENG06: 'https://deindu5ky.lightyy.com/group_pulloff', // 鲸腾：智能策略下架审核
  // 服务商城iframe地址
  ORDERMANAGE01: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-mall-pse/index.html#/bill/billManage', // 服务商城：服务商城订单管理
  SERVICEPRODUCT01: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-mall-pse/index.html#/product/typeManage', // 服务商城：分类管理
  SERVICEPRODUCT02: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-mall-pse/index.html#/product/commodityManage', // 服务商城：商品管理
  SERVICEPRODUCT03: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-mall-pse/index.html#/product/commodityTimeManage', // 服务商城：商品存续期管理
  SERVICEPRODUCT04: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-mall-pse/index.html#/product/productManage', // 服务商城：产品管理
  SERVICEPRODUCT05: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-mall-pse/index.html#/product/productTimeManage', // 服务商城：产品存续期管理
  // 统一支付iframe地址
  UNIFYPAYMENT01: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-payment/entrustquery.html', // 支付委托查询
  UNIFYPAYMENT02: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-payment/fileset.html', // 日终文件导入
  UNIFYPAYMENT03: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-payment/filecheck.html', // 支付委托查询
  UNIFYPAYMENT04: 'http://fulldev.yjifs.com:8080/h5-mock/h5-isee-payment/filecheckset.html', // 日终入账确认
  // 背景图设置模块不同版本名称区分
  LIVEBGSETTING_NAME: '直播背景图设置', // 通用版
  // LIVEBGSETTING_NAME: '投顾背景图设置' // 万和版

};
