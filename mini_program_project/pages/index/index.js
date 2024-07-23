Page({
  data: {
    info: null
  },

  onLoad: function () {
    this.getDataFromServer(this.handleServerResponse);
  },

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
        console.error('«Î«Û ß∞‹', err);
      }
    });
  },

  handleServerResponse: function (data) {
    this.setData({
      info: data
    });
  }
})