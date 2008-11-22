-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.0.22-Debian_0ubuntu6.06.10-log


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema timemanagement
--

CREATE DATABASE IF NOT EXISTS timemanagement;
USE timemanagement;

--
-- Definition of table `timemanagement`.`customer`
--

DROP TABLE IF EXISTS `timemanagement`.`customer`;
CREATE TABLE  `timemanagement`.`customer` (
  `cust_Id` tinyint(4) NOT NULL auto_increment,
  `cust_Name` varchar(50) default NULL,
  `cust_Address` varchar(50) default NULL,
  `cust_City` varchar(50) default NULL,
  `cust_State` varchar(50) default NULL,
  `cust_Contact` varchar(50) default NULL,
  `cust_Phone` varchar(50) default NULL,
  `cust_Fax` varchar(50) default NULL,
  PRIMARY KEY  (`cust_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timemanagement`.`customer`
--

/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
LOCK TABLES `customer` WRITE;
INSERT INTO `timemanagement`.`customer` VALUES  (1,'Atlas Tooling','9 Capital Ct','Braeside','Vic','Gopi',NULL,NULL),
 (2,'Bosch','Clayton','Clayton','Vic',NULL,NULL,NULL),
 (3,'Palm','South Road','Moorabbin',NULL,NULL,NULL,NULL);
UNLOCK TABLES;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`employee`
--

DROP TABLE IF EXISTS `timemanagement`.`employee`;
CREATE TABLE  `timemanagement`.`employee` (
  `empl_Id` tinyint(4) NOT NULL,
  `empl_First_Name` char(50) NOT NULL,
  `empl_Last_Name` char(50) NOT NULL,
  `empl_Position` varchar(50) default NULL,
  `joined_Date` date default NULL,
  `is_Active` tinyint(1) default NULL,
  PRIMARY KEY  (`empl_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timemanagement`.`employee`
--

/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
LOCK TABLES `employee` WRITE;
INSERT INTO `timemanagement`.`employee` VALUES  (105,'Pradeep','Meethale','Toolmaker',NULL,1),
 (106,'Anil','Thanappan','Toolmaker',NULL,1),
 (107,'Hareesh','kumar','Toolmaker',NULL,1);
UNLOCK TABLES;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`jobs`
--

DROP TABLE IF EXISTS `timemanagement`.`jobs`;
CREATE TABLE  `timemanagement`.`jobs` (
  `job_No` int(11) NOT NULL,
  `job_Name` char(50) default NULL,
  `job_Description` varchar(50) default NULL,
  `FK_customer_Id` tinyint(4) NOT NULL,
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

--
-- Dumping data for table `timemanagement`.`jobs`
--

/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
LOCK TABLES `jobs` WRITE;
INSERT INTO `timemanagement`.`jobs` VALUES  (1000,'Cleaning','Machine Cleaning',1,'','2000-01-01','2000-03-01','2000-01-01',0,'S'),
 (1001,'Machine Maintanance','Machine Maintanance',1,NULL,'2008-08-09',NULL,NULL,0,'S'),
 (1002,'Followup','Followup',1,NULL,NULL,NULL,NULL,0,'S'),
 (1003,'Unload','Unload Trucks',1,NULL,NULL,NULL,NULL,0,'S');
UNLOCK TABLES;
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`jobstatus`
--

DROP TABLE IF EXISTS `timemanagement`.`jobstatus`;
CREATE TABLE  `timemanagement`.`jobstatus` (
  `ID` int(2) NOT NULL auto_increment,
  `Description` varchar(40) default NULL,
  `Name` varchar(40) default NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timemanagement`.`jobstatus`
--

/*!40000 ALTER TABLE `jobstatus` DISABLE KEYS */;
LOCK TABLES `jobstatus` WRITE;
UNLOCK TABLES;
/*!40000 ALTER TABLE `jobstatus` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`partprocess`
--

DROP TABLE IF EXISTS `timemanagement`.`partprocess`;
CREATE TABLE  `timemanagement`.`partprocess` (
  `id` int(11) NOT NULL auto_increment,
  `FK_part_Id` tinyint(4) NOT NULL,
  `FK_process_Id` tinyint(4) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `FK_part_Id` (`FK_part_Id`),
  KEY `FK_process_Id` (`FK_process_Id`),
  CONSTRAINT `partprocess_ibfk_1` FOREIGN KEY (`FK_part_Id`) REFERENCES `parts` (`part_Id`),
  CONSTRAINT `partprocess_ibfk_2` FOREIGN KEY (`FK_process_Id`) REFERENCES `process` (`process_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timemanagement`.`partprocess`
--

/*!40000 ALTER TABLE `partprocess` DISABLE KEYS */;
LOCK TABLES `partprocess` WRITE;
INSERT INTO `timemanagement`.`partprocess` VALUES  (1,1,1),
 (2,1,2),
 (3,1,6),
 (4,1,8),
 (5,1,9),
 (6,1,10),
 (7,1,11),
 (8,1,12),
 (9,1,13),
 (10,1,16),
 (11,1,21),
 (12,1,22),
 (13,1,23),
 (14,1,25),
 (15,2,1),
 (16,2,2),
 (17,2,3),
 (18,2,4),
 (19,2,7),
 (20,2,23),
 (21,2,25),
 (22,3,2),
 (23,3,4),
 (24,3,6),
 (25,3,8),
 (26,3,9),
 (27,3,12),
 (28,3,25),
 (29,4,1),
 (30,4,2),
 (31,4,3),
 (32,4,6),
 (33,4,8),
 (34,4,9),
 (35,4,10),
 (36,4,11),
 (37,4,12),
 (38,4,13),
 (39,4,15),
 (40,4,16),
 (41,4,21),
 (42,4,22),
 (43,4,23),
 (44,4,24),
 (45,4,25),
 (46,5,1),
 (47,5,2),
 (48,5,6),
 (49,5,8),
 (50,5,9),
 (51,5,10),
 (52,5,11),
 (53,5,12),
 (54,5,16),
 (55,5,21),
 (56,5,22),
 (57,5,23),
 (58,5,24),
 (59,5,25),
 (60,6,1),
 (61,6,2),
 (62,6,6),
 (63,6,8),
 (64,6,9),
 (65,6,10),
 (66,6,11),
 (67,6,12),
 (68,6,14),
 (69,6,15),
 (70,6,16),
 (71,6,21),
 (72,6,22),
 (73,6,23),
 (74,6,24),
 (75,6,25),
 (77,8,1),
 (78,8,2),
 (79,8,6),
 (80,8,8),
 (81,8,9),
 (82,8,10),
 (83,8,11),
 (84,8,12),
 (85,8,14);
INSERT INTO `timemanagement`.`partprocess` VALUES  (86,8,15),
 (87,8,16),
 (88,8,21),
 (89,8,22),
 (90,8,23),
 (91,8,24),
 (92,8,25),
 (93,8,3),
 (94,8,5),
 (95,8,7),
 (96,9,1),
 (97,9,2),
 (98,9,3),
 (99,9,4),
 (100,9,7),
 (101,9,22),
 (102,9,25),
 (103,9,13);
UNLOCK TABLES;
/*!40000 ALTER TABLE `partprocess` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`parts`
--

DROP TABLE IF EXISTS `timemanagement`.`parts`;
CREATE TABLE  `timemanagement`.`parts` (
  `part_Id` tinyint(4) NOT NULL auto_increment,
  `part_Name` char(50) default NULL,
  PRIMARY KEY  (`part_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timemanagement`.`parts`
--

/*!40000 ALTER TABLE `parts` DISABLE KEYS */;
LOCK TABLES `parts` WRITE;
INSERT INTO `timemanagement`.`parts` VALUES  (1,'Top Plate'),
 (2,'Register Ring'),
 (3,'Top Insulation Plate'),
 (4,'Manifold Plate'),
 (5,'Malifold Backing Plate'),
 (6,'Cavity Plate'),
 (7,'Cavity Block'),
 (8,'Cavity Inserts'),
 (9,'Cavity Insert Backing'),
 (10,'Cavity Pins'),
 (11,'Taper Locks'),
 (12,'Core Blocks'),
 (13,'Core Plate'),
 (14,'Core Inserts'),
 (15,'Core Pins'),
 (16,'Slider'),
 (17,'Slider Pins'),
 (18,'Slider Pin Backing'),
 (19,'Core Pin Backing'),
 (20,'Heel Block'),
 (21,'Angle Pin'),
 (22,'Wear Plate'),
 (23,'Return Pin'),
 (24,'Ejector Pin'),
 (25,'Spacer'),
 (26,'Ejector Plate'),
 (27,'Ejector Retainer Plate'),
 (28,'Ejector Backing'),
 (29,'Wedge Block'),
 (30,'Support Block'),
 (31,'Bottom Plate'),
 (32,'Lifting Strap'),
 (33,'Mould leg'),
 (34,'Bench'),
 (35,'Machine'),
 (36,NULL);
UNLOCK TABLES;
/*!40000 ALTER TABLE `parts` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`process`
--

DROP TABLE IF EXISTS `timemanagement`.`process`;
CREATE TABLE  `timemanagement`.`process` (
  `process_Id` tinyint(4) NOT NULL auto_increment,
  `process_Name` char(50) default NULL,
  PRIMARY KEY  (`process_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `timemanagement`.`process`
--

/*!40000 ALTER TABLE `process` DISABLE KEYS */;
LOCK TABLES `process` WRITE;
INSERT INTO `timemanagement`.`process` VALUES  (1,'Bench-Milling'),
 (2,'Bench-Handwork'),
 (3,'Bench-Fitting'),
 (4,'Bench-Turning'),
 (5,'Bench-Polishing'),
 (6,'Bench-Other'),
 (7,'Turning'),
 (8,'NC-Vtek1'),
 (9,'NC-Vtek2'),
 (10,'NC-Okuma'),
 (11,'NC-Mazak'),
 (12,'NC-Programming'),
 (13,'NC-Other'),
 (14,'Wirecut'),
 (15,'EDM'),
 (16,'Planning'),
 (17,'Maintanance'),
 (18,'Bench-Cleaning'),
 (19,'NC-Cleaning'),
 (20,'Cleaning'),
 (21,'Bench-Cooling Hole'),
 (22,'Bench-Grinding'),
 (23,'Bench-Assembly'),
 (24,'Bench-Bedding'),
 (25,'Bench-Drilling');
UNLOCK TABLES;
/*!40000 ALTER TABLE `process` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`processes`
--

DROP TABLE IF EXISTS `timemanagement`.`processes`;
CREATE TABLE  `timemanagement`.`processes` (
  `id` tinyint(4) NOT NULL auto_increment,
  `description` varchar(40) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

--
-- Dumping data for table `timemanagement`.`processes`
--

/*!40000 ALTER TABLE `processes` DISABLE KEYS */;
LOCK TABLES `processes` WRITE;
INSERT INTO `timemanagement`.`processes` VALUES  (1,'Bench'),
 (2,'Cleaning'),
 (3,'Maintanance'),
 (4,'NC Milling'),
 (5,'Design'),
 (6,'Follow Up'),
 (7,'EDM Wirecutting'),
 (8,'EDM Spark');
UNLOCK TABLES;
/*!40000 ALTER TABLE `processes` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`timecard`
--

DROP TABLE IF EXISTS `timemanagement`.`timecard`;
CREATE TABLE  `timemanagement`.`timecard` (
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

--
-- Dumping data for table `timemanagement`.`timecard`
--

/*!40000 ALTER TABLE `timecard` DISABLE KEYS */;
LOCK TABLES `timecard` WRITE;
INSERT INTO `timemanagement`.`timecard` VALUES  (13,105,'07:30','16:00',1,9,2008,1,1,8),
 (14,105,'07:30','15:0',2,9,2008,1,1,7),
 (15,105,'07:30','16:0',4,9,2008,1,1,8),
 (16,105,'07:30','17:0',3,9,2008,1,1,9),
 (17,105,'07:30','16:00',1,10,2008,1,1,8),
 (18,105,'07:30','16:0',29,9,2008,1,1,8),
 (19,105,'07:30','16:00',2,10,2008,1,1,8),
 (20,105,'07:30','17:00',3,10,2008,1,1,9),
 (21,105,'07:30','17:0',4,10,2008,1,1,9),
 (22,105,'07:35','17:0',4,10,2008,1,1,8.91667),
 (23,105,'07:30','16:00',8,9,2008,1,1,8),
 (24,106,'07:30','05:30',7,9,2008,1,1,9.5),
 (25,106,'07:30','05:00',9,10,2008,1,1,9),
 (26,105,'07:30','16:00',10,10,2008,1,1,8),
 (27,105,'07:30','17:00',9,10,2008,1,1,9),
 (28,105,'07:30','16:0',8,10,2008,1,1,8),
 (29,105,'7:30','4:00',6,10,2008,1,1,8),
 (30,105,'7:30','4:00',7,10,2008,1,1,8),
 (31,105,'7:30','4:00',5,10,2008,1,1,8),
 (32,105,'7:30','5:00',30,9,2008,1,1,9),
 (33,105,'7:30','5:00',13,10,2008,1,1,9),
 (34,105,'7:30','5:00',14,10,2008,1,1,9),
 (35,105,'7:30','5:00',15,10,2008,1,1,9),
 (36,105,'7:30','7:00',16,10,2008,1,1,11);
INSERT INTO `timemanagement`.`timecard` VALUES  (39,105,'7:30','5:00',18,10,2008,1,1,9),
 (43,105,'7:30','5:00',17,10,2008,0,1,9),
 (44,105,'7:30','6:00',19,10,2008,0,1,10);
UNLOCK TABLES;
/*!40000 ALTER TABLE `timecard` ENABLE KEYS */;


--
-- Definition of table `timemanagement`.`work`
--

DROP TABLE IF EXISTS `timemanagement`.`work`;
CREATE TABLE  `timemanagement`.`work` (
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

--
-- Dumping data for table `timemanagement`.`work`
--

/*!40000 ALTER TABLE `work` DISABLE KEYS */;
LOCK TABLES `work` WRITE;
INSERT INTO `timemanagement`.`work` VALUES  (1,1000,1,1,10,2008,105,9,1,NULL),
 (2,1001,2,27,9,2008,105,8,NULL,NULL),
 (3,1002,1,28,9,2008,106,8,NULL,NULL),
 (4,1002,4,7,10,2008,106,3,NULL,NULL),
 (5,1003,5,8,10,2008,106,4,NULL,NULL),
 (6,1000,3,29,9,2008,106,3,NULL,NULL),
 (7,1000,1,8,10,2008,106,1,NULL,NULL),
 (8,1000,3,8,10,2008,106,1,NULL,NULL),
 (9,1000,2,8,10,2008,106,1,NULL,NULL),
 (10,1000,1,0,10,2008,105,4,NULL,NULL),
 (11,1000,1,9,10,2008,105,1,NULL,NULL),
 (12,1000,2,9,10,2008,105,1,NULL,NULL),
 (13,1000,6,NULL,10,2008,105,2,NULL,NULL),
 (14,1000,1,NULL,10,2008,105,NULL,NULL,NULL),
 (15,1000,4,NULL,10,2008,105,1,NULL,NULL),
 (16,1003,5,NULL,10,2008,105,2,NULL,NULL),
 (17,1000,1,10,10,2008,105,2,NULL,'Testing'),
 (18,1000,1,13,10,2008,105,5,NULL,'Tes'),
 (19,1000,2,13,10,2008,105,1,NULL,''),
 (20,1000,1,14,10,2008,105,1,NULL,NULL),
 (21,1001,4,14,10,2008,105,1,NULL,NULL),
 (22,1003,5,14,10,2008,105,3,NULL,NULL),
 (23,1002,7,14,10,2008,105,2,NULL,NULL),
 (24,1000,2,6,10,2008,105,1,NULL,NULL),
 (25,1002,6,6,10,2008,105,2,NULL,NULL);
INSERT INTO `timemanagement`.`work` VALUES  (26,1001,1,3,10,2008,105,1,NULL,NULL),
 (27,1003,3,3,10,2008,105,2,NULL,NULL),
 (28,1002,2,3,10,2008,105,3,NULL,NULL),
 (29,1002,2,2,10,2008,105,2,NULL,NULL),
 (30,1003,4,2,10,2008,105,2,NULL,NULL),
 (31,1000,8,2,10,2008,105,4,NULL,NULL),
 (32,1001,2,4,10,2008,105,2,NULL,NULL),
 (33,1000,1,4,10,2008,105,1,NULL,NULL),
 (34,1002,5,14,10,2008,105,0.5,NULL,'Design'),
 (35,1001,2,15,10,2008,105,2,NULL,'Mastercam'),
 (36,1003,3,15,10,2008,105,4,NULL,NULL),
 (37,1002,8,15,10,2008,105,1,NULL,NULL),
 (38,1002,2,16,10,2008,105,2,NULL,NULL),
 (39,1001,5,16,10,2008,105,2,NULL,NULL);
UNLOCK TABLES;
/*!40000 ALTER TABLE `work` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
