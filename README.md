# 每日打卡项目
这是我的每日打卡项目，目前仅写了hufe易班每日打卡

## HUFE易班打卡启动流程
1. fork或clone项目到自己的github上。
2. 项目创建后，去项目的settings页面，展开secrets，进入actions页面。![第二步图片](/images/enter_secrets_actions.jpg)
3. 添加用户名密码等变量
   1在当前页面点击New repository secret 按钮![点击nrs](/images/click_nrs.jpg)
   2添加属性，需要填的一共有三个属性，属性名请看下 ![添加新属性](/images/add_new_secret.jpg)
      - HUFE_USERNAME
        - 这个值就是学号
      - HUFE_PASSWORD
        - 默认密码是 hufe@身份证后六位
      - PHONE
4. 开启github actions ![开启actions](/images/start_actions.jpg)