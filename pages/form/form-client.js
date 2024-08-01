// pages/form/form.js

Page({
  data: {
    userInput: ''
  },

  // 处理用户输入
  onInput: function(e) {
    this.setData({
      userInput: e.detail.value
    });
  },

  // 提交表单
  onSubmit: function() {
    const that = this;
    wx.request({
      url: 'https://example.com/generate-wordcloud',  // 假设有一个后端接口来生成词云
      method: 'POST',
      data: {
        text: this.data.userInput
      },
      success: function(res) {
        that.setData({
          wordCloudImage: res.data.wordCloudUrl  // 假设返回词云图像的URL
        });
      }
    });
  }
});
