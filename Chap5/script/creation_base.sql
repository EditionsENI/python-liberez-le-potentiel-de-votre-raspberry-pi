CREATE TABLE `lecteurs` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nom` varchar(255) COLLATE utf8_bin NOT NULL,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `mot_de_passe` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
);
