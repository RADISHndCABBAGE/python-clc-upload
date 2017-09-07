/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost
 Source Database       : clc

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : utf-8

 Date: 09/07/2017 23:00:21 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `clc`
-- ----------------------------
DROP TABLE IF EXISTS `clc`;
CREATE TABLE `clc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(200) COLLATE gbk_bin DEFAULT NULL,
  `primary_index` varchar(5) COLLATE gbk_bin DEFAULT NULL,
  `secondary_index_start` varchar(5) COLLATE gbk_bin DEFAULT NULL,
  `secondary_index_end` varchar(5) COLLATE gbk_bin DEFAULT NULL,
  `third_index` varchar(5) COLLATE gbk_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=244 DEFAULT CHARSET=gbk COLLATE=gbk_bin;

SET FOREIGN_KEY_CHECKS = 1;
