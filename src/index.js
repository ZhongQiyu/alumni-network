// index.js

import React, { Component } from 'react'
import { View, Button } from '@tarojs/components'
import Taro from '@tarojs/taro'
import './index.scss'

export default class Index extends Component {
  state = {
    userInfo: {},
    wxData: null,
    feishuData: null
  }

  componentDidMount() {
    // 获取全局数据
    if (Taro.getApp().globalData.userInfo) {
      this.setState({
        userInfo: Taro.getApp().globalData.userInfo
      })
    } else {
      Taro.getApp().userInfoReadyCallback = res => {
        this.setState({
          userInfo: res.userInfo
        })
      }
    }
  }

  // 示例微信网络请求
  fetchDataFromWx = () => {
    Taro.request({
      url: 'https://example.com/api/data',
      method: 'GET',
      success: (res) => {
        this.setState({ wxData: res.data })
        console.log('微信请求成功', res.data)
      },
      fail: (err) => {
        console.error('微信请求失败', err)
      }
    })
  }

  // 示例飞书网络请求
  fetchDataFromFeishu = () => {
    Taro.request({
      url: 'https://open.feishu.cn/api/v1/data',
      method: 'GET',
      success: (res) => {
        this.setState({ feishuData: res.data })
        console.log('飞书请求成功', res.data)
      },
      fail: (err) => {
        console.error('飞书请求失败', err)
      }
    })
  }

  handleLogin = () => {
    Taro.showToast({
      title: '登录功能待实现',
      icon: 'none'
    })
  }

  handleGetCard = () => {
    Taro.navigateTo({
      url: '/pages/form/form'
    })
  }

  render() {
    return (
      <View className='index'>
        <View className='userinfo'>
          <Button onClick={this.handleLogin}>点击登录账号</Button>
        </View>
        <View className='section'>
          <Button onClick={this.handleGetCard}>立即领取</Button>
        </View>
        <View className='section'>
          <Button onClick={this.fetchDataFromWx}>获取微信数据</Button>
        </View>
        <View className='section'>
          <Button onClick={this.fetchDataFromFeishu}>获取飞书数据</Button>
        </View>
      </View>
    )
  }
}
