/*
SQLyog Community Edition- MySQL GUI v7.12 RC2
MySQL - 5.0.22-Debian_0ubuntu6.06.10-log : Database - timemanagement
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`management` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `management`;

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `cust_Id` int(11) NOT NULL auto_increment,
  `cust_Name` varchar(50) default NULL,
  `cust_Address` varchar(50) default NULL,
  `cust_City` varchar(50) default NULL,
  `cust_State` varchar(50) default NULL,
  `cust_Contact` varchar(50) default NULL,
  `cust_Phone` varchar(50) default NULL,
  `cust_Fax` varchar(50) default NULL,
  PRIMARY KEY  (`cust_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `empl_Id` tinyint(4) NOT NULL,
  `empl_First_Name` char(50) NOT NULL,
  `empl_Last_Name` char(50) NOT NULL,
  `empl_Position` varchar(50) default NULL,
  `joined_Date` date default NULL,
  `is_Active` tinyint(1) default NULL,
  PRIMARY KEY  (`empl_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `jobs` */

DROP TABLE IF EXISTS `jobs`;

CREATE TABLE `jobs` (
  `job_No` int(11) NOT NULL,
  `job_Name` char(50) default NULL,
  `job_Description` varchar(50) default NULL,
  `FK_customer_Id` int(11) NOT NULL,
  `cust_OrderNo` char(11) default NULL,
  `start_Date` date default NULL,
  `completion_Date` date default NULL,
  `completed_Date` date default NULL,
  `is_Rework` tinyint(1) unsigned NOT NULL default '0',
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`job_No`),
  KEY `FK_customer_Id` (`FK_customer_Id`),
  CONSTRAINT `jobs_ibfk_1` FOREIGN KEY (`FK_customer_Id`) REFERENCES `customer` (`cust_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `jobstatus` */

DROP TABLE IF EXISTS `jobstatus`;

CREATE TABLE `jobstatus` (
  `ID` int(2) NOT NULL auto_increment,
  `Description` varchar(40) default NULL,
  `Name` varchar(40) default NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Table structure for table `partprocess` */

DROP TABLE IF EXISTS `partprocess`;

CREATE TABLE `partprocess` (
  `id` int(11) NOT NULL auto_increment,
  `FK_part_Id` tinyint(4) NOT NULL,
  `FK_process_Id` tinyint(4) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `FK_part_Id` (`FK_part_Id`),
  KEY `FK_process_Id` (`FK_process_Id`),
  CONSTRAINT `partprocess_ibfk_1` FOREIGN KEY (`FK_part_Id`) REFERENCES `parts` (`part_Id`),
  CONSTRAINT `partprocess_ibfk_2` FOREIGN KEY (`FK_process_Id`) REFERENCES `process` (`process_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `parts` */

DROP TABLE IF EXISTS `parts`;

CREATE TABLE `parts` (
  `part_Id` tinyint(4) NOT NULL auto_increment,
  `part_Name` char(50) default NULL,
  PRIMARY KEY  (`part_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `process` */

DROP TABLE IF EXISTS `process`;

CREATE TABLE `process` (
  `process_Id` tinyint(4) NOT NULL auto_increment,
  `process_Name` char(50) default NULL,
  PRIMARY KEY  (`process_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `processes` */

DROP TABLE IF EXISTS `processes`;

CREATE TABLE `processes` (
  `id` tinyint(4) NOT NULL auto_increment,
  `description` varchar(40) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/*Table structure for table `timecard` */

DROP TABLE IF EXISTS `timecard`;

CREATE TABLE `timecard` (
  `time_Id` tinyint(4) NOT NULL auto_increment,
  `FK_empl_Id` tinyint(4) NOT NULL,
  `time_In` char(6) NOT NULL,
  `time_Out` char(6) NOT NULL,
  `worked_Day` int(4) default NULL,
  `worked_Month` int(4) default NULL,
  `worked_Year` int(4) default NULL,
  `isDataEntered` tinyint(1) NOT NULL,
  `lunchBreak` tinyint(1) NOT NULL default '1',
  `totHours` float default '0',
  PRIMARY KEY  (`time_Id`),
  KEY `FK_empl_Id` (`FK_empl_Id`),
  CONSTRAINT `timecard_ibfk_1` FOREIGN KEY (`FK_empl_Id`) REFERENCES `employee` (`empl_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_Id` int(11) NOT NULL auto_increment,
  `FK_job_No` int(11) NOT NULL,
  `FK_process_ID` tinyint(4) NOT NULL,
  `worked_Day` int(2) default NULL,
  `worked_Month` int(2) NOT NULL,
  `worked_Year` int(4) default NULL,
  `FK_empl_Id` tinyint(4) NOT NULL,
  `worked_Hours` double unsigned default NULL,
  `is_Overtime` tinyint(1) default NULL,
  `notes` varchar(100) default NULL,
  PRIMARY KEY  (`work_Id`),
  KEY `FK_job_No` (`FK_job_No`),
  KEY `FK_process_ID` (`FK_process_ID`),
  KEY `FK_empl_Id` (`FK_empl_Id`),
  CONSTRAINT `work_ibfk_1` FOREIGN KEY (`FK_job_No`) REFERENCES `jobs` (`job_No`),
  CONSTRAINT `work_ibfk_2` FOREIGN KEY (`FK_process_ID`) REFERENCES `processes` (`id`),
  CONSTRAINT `work_ibfk_3` FOREIGN KEY (`FK_empl_Id`) REFERENCES `employee` (`empl_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;