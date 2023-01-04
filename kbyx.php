<!DOCTYPE html>
<html>
<head>
  <title>恐怖游戏</title>
</head>
<body>
  <h1>恐怖游戏</h1>
  <p>你来到一个古老的山洞，里面有三扇门：红色、蓝色和绿色。你只能选择一扇门，但你不知道后果会是什么。</p>
  <form>
    <input type="radio" name="door" value="red">红色门<br>
    <input type="radio" name="door" value="blue">蓝色门<br>
    <input type="radio" name="door" value="green">绿色门<br>
    <input type="submit" value="提交">
  </form>
  <?php
    if (isset($_GET['door'])) {
      $door = $_GET['door'];
      if ($door == 'red') {
        echo "<p>你选择了红色门，你发现了一个宝箱，里面装满了金钱和宝石！你得到了财富！</p>";
      } elseif ($door == 'blue') {
        echo "<p>你选择了蓝色门，你发现了一个可怕的怪物！你被吓坏了！</p>";
      } elseif ($door == 'green') {
        echo "<p>你选择了绿色门，你发现了一个神秘的老人，他赐予了你一个神奇的力量！</p>";
      }
    }
  ?>
</body>
</html>