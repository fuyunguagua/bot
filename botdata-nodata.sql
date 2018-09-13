-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: botdata
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `10h_fid`
--

DROP TABLE IF EXISTS `10h_fid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `10h_fid` (
  `ip_src` char(15) CHARACTER SET utf8 NOT NULL,
  `ip_dst` char(15) CHARACTER SET utf8 NOT NULL,
  `port_dst` int(11) NOT NULL,
  `mints` double(16,6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `1h_fid`
--

DROP TABLE IF EXISTS `1h_fid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `1h_fid` (
  `ip_src` char(15) CHARACTER SET utf8 NOT NULL,
  `ip_dst` char(15) CHARACTER SET utf8 NOT NULL,
  `port_dst` int(11) NOT NULL,
  `mints` double(16,6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ares`
--

DROP TABLE IF EXISTS `ares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ares` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4702100 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `athena`
--

DROP TABLE IF EXISTS `athena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `athena` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3585851 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `blackenergy`
--

DROP TABLE IF EXISTS `blackenergy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blackenergy` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4791458 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `buffer`
--

DROP TABLE IF EXISTS `buffer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buffer` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10153246 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cflow`
--

DROP TABLE IF EXISTS `cflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cflow` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IP_SRC` varchar(20) DEFAULT NULL,
  `IP_DST` varchar(20) DEFAULT NULL,
  `PORT_SRC` int(11) DEFAULT NULL,
  `PORT_DST` int(11) DEFAULT NULL,
  `FLOWS` int(11) NOT NULL,
  `FPH_13` varchar(100) NOT NULL,
  `PPF_13` varchar(100) NOT NULL,
  `BPP_13` varchar(100) NOT NULL,
  `BPS_13` varchar(100) NOT NULL,
  `NOTE` char(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1665791 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cflow_52`
--

DROP TABLE IF EXISTS `cflow_52`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cflow_52` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IP_SRC` varchar(20) DEFAULT NULL,
  `IP_DST` varchar(20) DEFAULT NULL,
  `PORT_SRC` int(11) DEFAULT NULL,
  `PORT_DST` int(11) DEFAULT NULL,
  `FLOWS` int(11) NOT NULL,
  `FPH_13` varchar(100) NOT NULL,
  `PPF_13` varchar(100) NOT NULL,
  `BPP_13` varchar(100) NOT NULL,
  `BPS_13` varchar(100) NOT NULL,
  `NOTE` char(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1665789 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `common`
--

DROP TABLE IF EXISTS `common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `common` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` varchar(30) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `filterip`
--

DROP TABLE IF EXISTS `filterip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filterip` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IP` char(15) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13999 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mirai`
--

DROP TABLE IF EXISTS `mirai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mirai` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=23172940 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `new_ares`
--

DROP TABLE IF EXISTS `new_ares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_ares` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` varchar(30) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2267518 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `new_athena`
--

DROP TABLE IF EXISTS `new_athena`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_athena` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` varchar(30) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=129443 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `new_blackenergy`
--

DROP TABLE IF EXISTS `new_blackenergy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_blackenergy` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` varchar(30) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4176734 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `new_cflow`
--

DROP TABLE IF EXISTS `new_cflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_cflow` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `IP_SRC` varchar(20) DEFAULT NULL,
  `IP_DST` varchar(20) DEFAULT NULL,
  `PORT_SRC` int(11) DEFAULT NULL,
  `PORT_DST` int(11) DEFAULT NULL,
  `FLOWS` int(11) NOT NULL,
  `FPH_13` varchar(100) NOT NULL,
  `PPF_13` varchar(100) NOT NULL,
  `BPP_13` varchar(100) NOT NULL,
  `BPS_13` varchar(100) NOT NULL,
  `note` int(4) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1665789 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `new_mirai`
--

DROP TABLE IF EXISTS `new_mirai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_mirai` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3861019 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `new_zeus`
--

DROP TABLE IF EXISTS `new_zeus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_zeus` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` varchar(30) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=729435 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `newpackets`
--

DROP TABLE IF EXISTS `newpackets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `newpackets` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` varchar(30) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=77013888 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `newpacketsfilted`
--

DROP TABLE IF EXISTS `newpacketsfilted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `newpacketsfilted` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=27573642 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `packets`
--

DROP TABLE IF EXISTS `packets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `packets` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1410707002 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `packetsfilted`
--

DROP TABLE IF EXISTS `packetsfilted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `packetsfilted` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=98295348 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `zeus`
--

DROP TABLE IF EXISTS `zeus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zeus` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TIMESTAMP` double(16,6) NOT NULL,
  `LENGTH` int(11) NOT NULL,
  `IP_SRC` char(15) NOT NULL,
  `IP_DST` char(15) NOT NULL,
  `PORT_SRC` int(11) NOT NULL,
  `PORT_DST` int(11) NOT NULL,
  `FLAG` char(5) DEFAULT NULL,
  `ISBOT` int(11) DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2013373 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-09 14:16:40
