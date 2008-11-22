/*
SQLyog Community Edition- MySQL GUI v7.12 RC2
MySQL - 5.0.22-Debian_0ubuntu6.06.10-log : Database - timemanagement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`timemanagement` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `timemanagement`;

/*Data for the table `processes` */

insert  into `processes`(`id`,`description`) values (1,'Bench'),(2,'Cleaning'),(3,'Maintanance'),(4,'NC Milling'),(5,'Design'),(6,'Follow Up'),(7,'EDM Wirecutting'),(8,'EDM Spark');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
