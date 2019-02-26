#include <getopt.h>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

const char* const kFilePath = "./12-1_test";

using namespace std;

void ReadLastKLine(const string& path)
{
	int k = 10;
	ifstream ifile(kFilePath, ifstream::in);
	string tmp[k];
	if (!ifile.is_open() && !ifile.good()) {
		//error
	}
	string line;
	int size = 0;
	while (!ifile.eof() && getline(ifile, line)) {
		tmp[size%k] = line;
		size++;
	}
	int start = (size > k) ? (size % k) : 0;
	int count = min(size, k);
	for (int i = 0; i < count; i++) {
		cout << tmp[(start + i) % k] << endl;
	}
	ifile.close();
	return;
}


int main(int argc, char* argv[])
{
	string path = "";
	int c = 0;
	while ((c = getopt_long(argc, argv, "f:", NULL, NULL)) != -1) {
		switch (c) {
			case 'f':
				path = optarg;
				ReadLastKLine(path);
				break;
			default:
				return -1;
				break;
		}
	}
}
