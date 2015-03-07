<?php
namespace NethServer\Module\Dashboard\Applications;

/**
 * tt-rss web interface
 *
 * @author stephane de labrusse
 */
class ttrss extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "tt-rss web interface";
    }

    public function getInfo()
    {
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "https://".$host[0]."/tt-rss/"
         );
    }
}


