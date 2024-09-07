Page({
  data: {},

  onLoad() {
    // 页面加载时的初始化逻辑
    console.log('页面已加载');
  },

  handleNavItemTap(event) {
    const navItem = event.currentTarget.dataset.navItem;
    console.log(`你点击了: ${navItem}`);

    // 根据点击的项跳转到相应的页面
    if (navItem === '首页') {
      wx.navigateTo({
        url: '/pages/index/index',
      });
    } else if (navItem === '组织') {
      wx.navigateTo({
        url: '/pages/organization/organization',
      });
    } else if (navItem === '我的') {
      wx.navigateTo({
        url: '/pages/profile/profile',
      });
    }
  },

  handleLogin() {
    // 登录处理逻辑
    wx.showToast({
      title: '登录按钮被点击',
      icon: 'success'
    });
    // 此处可以调用登录接口或跳转到登录页面
  },

  handleCardApplication() {
    // 跳转到校友卡申领页面的处理逻辑
    wx.navigateTo({
      url: '/pages/card-application/card-application',
    });
  }
});
