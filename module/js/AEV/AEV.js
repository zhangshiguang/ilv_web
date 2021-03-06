/***************************************************************************************************
 * 名称：AEV an easy video control 简单视频控制器
***************************************************************************************************/
AEV = {};
/***************************************************************************************************
 * 1 AEE.show(pyDir,flvDir,width,height) 显示视频
 * swfDirswf相对网页位置 pyDir网页相对swf位置 flvDir视频相对网页位置 宽度 高度
***************************************************************************************************/
AEV.show = function(swfDir,pyDir,flvDir,width,height){
    if(!swfDir) swfDir = "Flvplayer.swf";
    if(!pyDir) pyDir = "";
    if(!flvDir) flvDir = "1.flv";
    if(!width) width = "660";
    if(!height) height = "530";
    var html = "";
    html += ' <embed src="'+swfDir+'" width="'+width+'" height="'+height+'" quality="high"'
          + ' FlashVars="vcastr_file='+pyDir+flvDir+'&LogoText=www.js0971.com&BufferTime=3"'
          + ' pluginspage="http://www.macromedia.com/go/getflashplayer"'
          + ' type="application/x-shockwave-flash" scale="exactfit" menu="false"'
          + ' wmode="transparent">'
          + '</embed>';
    document.open();
    document.write(html);
    document.close();
}
