<?php    //查询用户是否上线了    
$userip = @$_POST['ip'];    
$usermac = @$_POST['mac'];​    
if (!$userip || !$usermac) {  
exit;   
}    /* 判断该用户是否已经放行 */    
$cmd = '/sbin/app_auth_hook.elf -f ' . $userip;    #直接进行命令拼接
$res = exec($cmd, $out, $status);    /* 如果已经上线成功 */    
if (strstr($out[0], "status:1")) {        
echo 'true'; 
}
?>
