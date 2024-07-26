import React from 'react';

function MyPage() {
  return (
    <div className="container">
      <nav>
        <ul>
          <li>首页</li>
          <li>组织</li>
          <li>我的</li>
        </ul>
      </nav>
      <main>
        <section className="personal-center">
          <p>个人中心</p>
          <button>点击登录账号</button>
        </section>
        <section className="card-application">
          <h3>百森俱乐部校友卡</h3>
          <button>点击跳转申领校友卡</button>
          <p>立即领取</p>
          <p>校友会联系方式: ...</p>
        </section>
      </main>
      <footer>
        Copyright © 2024 by Boston Consulting Group. All rights reserved.
      </footer>
    </div>
  );
}

export default MyPage;