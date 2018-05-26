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
        return "Tiny Tiny RSS";
    }

    public function getInfo()
    {
        $customDomainName = $this->getPlatform()->getDatabase('configuration')->getProp('tt-rss','DomainName');
        $DomainName = $this->getPlatform()->getDatabase('configuration')->getType('DomainName');
        return array(
            'url' => "https://".($customDomainName ?: $DomainName)."/tt-rss/"
        );
    }
}
