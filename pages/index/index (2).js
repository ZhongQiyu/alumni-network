Page({
  data: {
    info: null
  },

  onLoad: function () {
    this.getDataFromServer(this.handleServerResponse);
  },

  // 获取服务器数据的方法
  getDataFromServer: function (callback) {
    wx.request({
      url: 'https://example.com/api/data',
      method: 'GET',
      success: function (res) {
        if (callback) {
          callback(res.data);
        }
      },
      fail: function (err) {
        console.error('请求失败', err);
      }
    });
  },

  // 处理服务器响应的回调函数
  handleServerResponse: function (data) {
    this.setData({
      info: data
    });
  }
})