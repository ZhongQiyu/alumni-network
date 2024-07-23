App({
  onLaunch: function () {
    // չʾ���ش洢����
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // ��¼
    wx.login({
      success: res => {
        // ���� res.code ����̨��ȡ openId, sessionKey, unionId
        console.log('΢�ŵ�¼�ɹ�', res)
        // �����ȡ���� openId
        this.globalData.openId = res.code
      }
    })

    // ��ȡ�û���Ϣ
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // �Ѿ���Ȩ������ֱ�ӵ��� getUserInfo ��ȡͷ���ǳƣ����ᵯ��
          wx.getUserInfo({
            success: res => {
              // ���Խ� res ���͸���̨����� unionId
              this.globalData.userInfo = res.userInfo

              // ���� getUserInfo ���������󣬿��ܻ��� Page.onLoad ֮��ŷ���
              // ���Դ˴����� callback �Է�ֹ�������
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },

  onShow: function (options) {
    console.log('С������ʾ', options)
  },

  onHide: function () {
    console.log('С��������')
  },

  onError: function (msg) {
    console.error('С�������', msg)
  },

  globalData: {
    userInfo: null,
    openId: null
  },

  requestWx: function (url, method, data, success, fail) {
    wx.request({
      url: url,
      method: method,
      data: data,
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.statusCode == 200) {
          success(res.data)
        } else {
          fail(res)
        }
      },
      fail: function (err) {
        fail(err)
      }
    })
  },

  requestFeishu: function (url, method, data, success, fail) {
    wx.request({
      url: url,
      method: method,
      data: data,
      header: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_FEISHU_ACCESS_TOKEN'
      },
      success: function (res) {
        if (res.statusCode == 200) {
          success(res.data)
        } else {
          fail(res)
        }
      },
      fail: function (err) {
        fail(err)
      }
    })
  }
})