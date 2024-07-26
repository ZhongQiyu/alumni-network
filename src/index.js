Page({
  data: {
    showForm: false,
  },
  login() {
    wx.showToast({
      title: '登录功能待实现',
      icon: 'none'
    });
  },
  getCard() {
    this.setData({
      showForm: true
    });
  },
  onSubmit(e) {
    wx.showToast({
      title: '表单提交成功',
      icon: 'success'
    });
    this.setData({
      showForm: false
    });
  }
});
