-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: pythontkinter
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chitiet`
--

DROP TABLE IF EXISTS `chitiet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitiet` (
  `MaNV` varchar(45) NOT NULL,
  `ChucVu` varchar(45) NOT NULL,
  `HSLuong` int NOT NULL,
  `MucDoCV` varchar(45) NOT NULL,
  PRIMARY KEY (`MaNV`),
  CONSTRAINT `MaNV` FOREIGN KEY (`MaNV`) REFERENCES `nhanvien` (`MaNV`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitiet`
--

LOCK TABLES `chitiet` WRITE;
/*!40000 ALTER TABLE `chitiet` DISABLE KEYS */;
INSERT INTO `chitiet` VALUES ('001','NV',4,'C1'),('002','NV',5,'C3'),('003','NV',3,'C2'),('004','NV',2,'C1'),('005','NV',6,'C3'),('006','TL',6,'B2'),('007','PP',5,'B2'),('008','PGD',7,'A2'),('009','PP',7,'B2'),('010','NV',6,'C3'),('011','NV',5,'C2'),('012','NV',4,'C3'),('013','NV',7,'C3'),('014','TX',4,'B3'),('015','TK',4,'C2'),('016','NV',5,'C1'),('017','PP',8,'B2'),('018','NV',3,'C2'),('019','PGD',7,'A2'),('020','TK',4,'C2'),('021','TL',5,'B2'),('022','TP',7,'A3'),('023','NV',4,'C2'),('024','NV',4,'C3'),('025','NV',3,'C3'),('026','TL',4,'B2'),('027','TX',5,'B3'),('028','NV',7,'C3'),('029','NV',3,'C3'),('030','NV',3,'C3'),('031','NV',4,'C2'),('032','PP',6,'B3'),('033','TP',7,'A3'),('034','NV',5,'C3'),('035','PP',6,'B3'),('036','TK',4,'B1'),('037','NV',3,'C2'),('038','TK',4,'B1'),('039','NV',4,'C2'),('040','TP',7,'A3'),('041','PGD',8,'A2'),('042','NV',5,'C3'),('043','TK',4,'B1'),('044','NV',4,'C3'),('045','NV',3,'C1'),('046','NV',2,'C1'),('047','TP',8,'A2'),('048','NV',5,'C3'),('049','NV',3,'C2'),('050','NV',6,'C3'),('051','NV',4,'C2'),('052','PP',7,'B3'),('053','NV',2,'C2'),('054','NV',4,'C2'),('055','NV',3,'C2'),('056','NV',4,'C3'),('057','GD',9,'AC'),('058','NV',4,'C2'),('059','NV',3,'C1'),('060','TP',7,'A3');
/*!40000 ALTER TABLE `chitiet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hschucvu`
--

DROP TABLE IF EXISTS `hschucvu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hschucvu` (
  `ChucVu` varchar(45) NOT NULL,
  `HSCV` double NOT NULL,
  PRIMARY KEY (`ChucVu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hschucvu`
--

LOCK TABLES `hschucvu` WRITE;
/*!40000 ALTER TABLE `hschucvu` DISABLE KEYS */;
INSERT INTO `hschucvu` VALUES ('GD',3),('NV',1),('PGD',2.2),('PP',1.5),('TK',1.2),('TL',1.5),('TP',2),('TX',1.2);
/*!40000 ALTER TABLE `hschucvu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhanvien` (
  `MaNV` varchar(45) NOT NULL,
  `Ho` varchar(45) NOT NULL,
  `Ten` varchar(45) NOT NULL,
  `Phai` tinyint DEFAULT NULL,
  `NTNS` date NOT NULL,
  `NgayBatDau` date NOT NULL,
  `MaPB` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`MaNV`),
  KEY `MaPB_idx` (`MaPB`),
  CONSTRAINT `MaPB` FOREIGN KEY (`MaPB`) REFERENCES `phongban` (`MaPB`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
INSERT INTO `nhanvien` VALUES ('001','Lai Van','Sam',0,'1966-01-01','1990-04-30','VP'),('002','Tran Van ','Minh',0,'1965-02-23','1990-05-10','VP'),('003','Toang Canh','Son',0,'1963-01-12','1996-10-24','TK'),('004','Ngo Viet ','Huong',0,'1977-02-11','1997-06-04','TK'),('005','Mai Tho','Loan',1,'1977-02-11','1997-06-04','TK'),('006','Mac Xuan','Tien',0,'1963-04-12','1992-03-28','TK'),('007','Vu Hoai','Anh',0,'1968-06-15','1993-03-09','KH'),('008','Tran Thanh','Khanh',0,'1942-07-15','1985-10-11','KH'),('009','Nguyen Hong','Hanh',1,'1962-01-13','1987-06-06','KT'),('010','Le Thi','Huong',1,'1962-05-23','1988-06-06','KT'),('011','Lam Quoc','Khanh',0,'1963-06-21','1991-09-27','KT'),('012','Nguyen Hong','Van',1,'1976-05-11','1995-05-05','TK'),('013','Nguyen Minh','Quan',0,'1951-06-13','1987-05-05','VP'),('014','Trang Phi','Hung',0,'1953-03-23','1996-07-07','VP'),('015','Tran Nguyet','Minh',1,'1963-09-19','1995-10-10','VP'),('016','Nguyen Ngoc','Hien',1,'1961-03-14','1990-04-08','VP'),('017','Do Anh','Hang',0,'1960-01-11','1979-05-05','VP'),('018','Ninh Tho','Tam',1,'1962-03-04','1995-05-05','TC'),('019','Nguyen Kim','Toan',1,'1960-09-01','1990-07-31','TC'),('020','Nguyen Bich','Lien',1,'1969-03-03','1996-12-16','TC'),('021','Huynh Bach','Tuyet',1,'1968-03-07','1994-05-23','KH'),('022','Le Phong','Thanh',1,'1957-02-12','1981-05-05','KH'),('023','Tai The ','Khanh',0,'1969-05-23','1993-09-15','KH'),('024','Bui Son','Hai',0,'1951-03-14','1990-05-08','TC'),('025','Luu Vu','Cam',0,'1970-06-17','1995-08-22','TK'),('026','Doan Thi','Chi',0,'1960-05-12','1994-10-30','TC'),('027','Tran Quang','Thanh',0,'1963-09-14','1992-05-05','TK'),('028','Truong Le','Xuan',1,'1968-04-13','1994-05-23','KT'),('029','Nguyen Van','Thanh',0,'1969-09-02','1996-02-08','TC'),('030','Dang Van','Thuy',0,'1968-01-01','1992-08-23','TK'),('031','Nguyen Van','Thanh',0,'1979-02-02','1994-05-23','KH'),('032','Lam Van','Tuan',0,'1969-02-12','1993-09-09','TK'),('033','Hoang Ngoc','Thanh',0,'1944-05-13','1978-03-09','VP'),('034','Nguyen Van','Nuoi',0,'1970-04-23','1990-10-02','TK'),('035','Do Ninh','Viet',0,'1945-04-12','1985-07-31','TC'),('036','Le Trung','Binh',0,'1977-04-13','1997-05-30','TK'),('037','Tran The','Duyet',0,'1970-04-14','1996-04-26','KH'),('038','Le Bich','Phuong',1,'1974-03-13','1995-08-04','KH'),('039','Mai Van','Duoc',0,'1960-04-14','1993-10-04','TC'),('040','Truong Xuan','Hong',0,'1940-05-15','1979-04-28','TC'),('041','Huynh Ngoc','Quanh',0,'1964-05-23','1990-05-30','TK'),('042','Dao Thanh','Huong',1,'1969-03-12','1993-08-08','TK'),('043','Pham Hoai','Nam',1,'1978-06-15','1992-07-28','VP'),('044','Le Thi My','Linh',1,'1971-09-19','1995-05-30','TK'),('045','Pham The','Dung',0,'1980-05-23','1997-12-30','TK'),('046','Hoang Thanh','Trang',1,'1970-03-12','1997-03-03','KT'),('047','Nguyen Van','Hien',0,'1960-06-15','1988-05-05','TK'),('048','Tran Nguyet','Nga',1,'1965-07-12','1993-04-26','TK'),('049','Mai Thi Hong','Xuan',1,'1962-06-02','1995-09-09','VP'),('050','Nguyen Thi','Nam',1,'1960-07-06','1987-06-06','KT'),('051','Ton Thi Thanh','Nhan',1,'1965-06-14','1993-10-04','TC'),('052','Nguyen To','Uyen',1,'1963-06-05','1990-10-07','TK'),('053','Luong Anh','Tuyen',1,'1975-01-23','1997-10-02','KT'),('054','Doan Van','Thanh',0,'1971-03-24','1993-06-06','VP'),('055','Luong Van','Chanh',0,'1963-05-20','1997-01-12','TK'),('056','Truong Tuong','Nhat',0,'1972-12-25','1994-05-23','KH'),('057','Nguyen Xuan','Phuong',0,'1960-04-14','1986-01-05','TK'),('058','Vo Ngoc','Quang',0,'1960-02-12','1990-10-07','TK'),('059','Nguyen Thanh','Thuy',1,'1960-05-19','1996-07-07','TK'),('060','Nguyen Trong ','Son',0,'1941-05-20','1989-07-22','KT'),('061','Nguyen Van ','A',1,'2020-11-14','2021-11-14','KT');
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phongban`
--

DROP TABLE IF EXISTS `phongban`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phongban` (
  `MaPB` varchar(45) NOT NULL,
  `TenPB` varchar(45) NOT NULL,
  PRIMARY KEY (`MaPB`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phongban`
--

LOCK TABLES `phongban` WRITE;
/*!40000 ALTER TABLE `phongban` DISABLE KEYS */;
INSERT INTO `phongban` VALUES ('KH','Phong Kinh te Ke hoach'),('KT','Phong Ke toan Tai chanh'),('TC','Phong To chuc Nhan so'),('TK','Phong Ky thuat Thiet ke'),('VP','Van phong Xi nghiep');
/*!40000 ALTER TABLE `phongban` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-04 23:18:20
