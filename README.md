# fastlink-autologin

> 某个网站✈️的自动登录签到脚本，[随缘aff(推广)](https://v01.fl-aff.com/auth/register?code=A2qb)

# 使用方法

1. **fork 本仓库**

   **<img src="README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2011.45.01.png" alt="截屏2023-02-07 11.45.01" style="zoom:50%;" />**

2. **设置仓库的 Github Actions**

   * 点击 "I understand"

   ![截屏2023-02-07 11.46.33](README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2011.46.33.png)

   * 整个项目只有一个workflow，其中包含一个定时触发条件，点击 Enable workflow 开启定时触发

   ![截屏2023-02-07 11.47.50](README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2011.47.50.png)

   * 更多有关GitHub Action内容请参考[官方文档](https://docs.github.com/en/actions)
   * 有关workflow语法请参考[workflow-syntax-for-github-actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

3. **配置登录信息**

   * 进入仓库的设置中，选择Actions设置，点击右方按钮设置仓库密钥。（**设置内容仅对自己可见，同时在workflow输出中也不可见**）

     有关内容可以参考[GitHub Actions 第11天：密码（Secrets）](https://qiwihui.com/qiwihui-blog-94/)

   ![截屏2023-02-07 11.51.47](README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2011.51.47.png)

   * 需要设置的内容如下，包含登录邮箱和登录密码

   ![截屏2023-02-07 12.00.14](README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2012.00.14.png)

4. 触发workflow

   * 通过三种方式可以触发：push、定时任务、在actions页面手动触发

     ```yaml
     on:
       push:
       schedule:
         - cron: '0 22 * * *'
     
       # 允许在 github actions 页面手动触发
       workflow_dispatch:
     ```

   * 定时任务使用的是UTC时间，所以实际触发时间为北京时间6:00

   * 可以通过push任意的commit来触发该任务，检测是否能正常触发

   * 在actions页面点击按钮手动触发任务

     ![截屏2023-02-20 21.08.39](README.assets/%E6%88%AA%E5%B1%8F2023-02-20%2021.08.39.png)

5. 检查任务执行情况

   * 在actions中可以查看任务历史

     ![截屏2023-02-07 12.10.59](README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2012.10.59.png)

   * 点击单个job，查看是否执行成功

     ![截屏2023-02-07 12.12.43](README.assets/%E6%88%AA%E5%B1%8F2023-02-07%2012.12.43.png)