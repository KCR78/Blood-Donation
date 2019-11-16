-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2019 at 01:30 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blood_donation`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(12) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'Krushna Chandra Rout', 'krushnachandrarout15@gmail.com', '7504880671', 'Hi...Finally the website is working. Thank God. My Mini Project is done.', '2019-11-03 16:59:50'),
(2, 'this', 'this@gmail.com', '0987654321', 'abto hoja bhai.....', '2019-11-03 17:39:41'),
(3, 'Bikas', 'bikas@gmail.com', '0987654321', 'hello, greate website.', '2019-11-03 20:53:32');

-- --------------------------------------------------------

--
-- Table structure for table `donor`
--

CREATE TABLE `donor` (
  `sno` int(12) NOT NULL,
  `name` text NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int(10) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donor`
--

INSERT INTO `donor` (`sno`, `name`, `gender`, `age`, `bloodgroup`, `phone_num`, `email`, `address`, `date`) VALUES
(1, 'Krushna Chandra Rout', 'Male', 24, 'AB+', '7504880671', 'krushnachandrarout15@gmail.com', 'Pondicherry University', '2019-11-03 23:44:21'),
(7, 'Sagarika Adhikary', 'Female', 21, 'B+', '0987654321', '', 'Pondicherry University, Pondicherry', '2019-11-04 05:48:46');

-- --------------------------------------------------------

--
-- Table structure for table `recipient`
--

CREATE TABLE `recipient` (
  `sno` int(12) NOT NULL,
  `name` text NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` int(10) NOT NULL,
  `bloodgroup` varchar(10) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recipient`
--

INSERT INTO `recipient` (`sno`, `name`, `gender`, `age`, `bloodgroup`, `phone_num`, `email`, `address`, `date`) VALUES
(1, 'Krushna Chandra Rout', 'Male', 24, 'AB+', '7504880671', 'krushnachandrarout15@gmail.com', 'Pondicherry University', '2019-11-04 00:22:19'),
(3, 'Sagarika Adhikary', 'Female', 21, 'B+', '0987654321', 'sagarika@gmail.com', 'Pondichery University', '2019-11-04 02:35:55');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `donor`
--
ALTER TABLE `donor`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `recipient`
--
ALTER TABLE `recipient`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `donor`
--
ALTER TABLE `donor`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `recipient`
--
ALTER TABLE `recipient`
  MODIFY `sno` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
