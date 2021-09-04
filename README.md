# Buzzle Bee

## About

This is a program designed to allow players to "buzz in" to some type of game show.

It is designed with a Jeopardy-style game in mind, but could be applied to many scenarios.

It is also designed with the idea of a locally played game -- all on the same network -- although
with the correct hosting it should work fine over the internet (note, however, that security
measures were not necessarily taken with this alternative setup in mind).

This is perfectly free and fine to use for personal use, but please contact for any commerical use.

## Screenshots

![HTML Page](https://i.imgur.com/9DWuPDh.png)

![Queue GUI](https://i.imgur.com/O8vajUi.png)

![Server Console](https://i.imgur.com/cIDc2LU.png)

## Usage

This is a rather basic Python setup, so usage should be straight-forward.

It was written with Python 3.6.2 as the development environment.

The following are the libraries that are required, which may be needed to install with "pip install XXX":
	tkinter
	threading
	flask

The server will host at an address specififed in a file named "address.txt" that is located in the same directory
as the main python file. If you have not set up a file, then it will create the file, with the default local host
address of "127.0.0.1"

## Contact

Feel free to contact me at benjamin.w.massey@gmail.com with any questions / inquiries.