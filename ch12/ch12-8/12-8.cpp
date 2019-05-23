#include <iostream>
#include <map>

using namespace std;
class Node {
public:
	explicit Node();
	virtual ~Node();
	void setLeftPtr(Node* node_ptr) {this->left_ptr = node_ptr; }
	void setRightPtr(Node* node_ptr) {this->right_ptr = node_ptr; }
	Node* getLeftPtr() { return this->left_ptr; }
	Node* getRightPtr() { return this->right_ptr; }

private:
	Node* left_ptr;
	Node* right_ptr;
};

Node::Node():left_ptr(NULL), right_ptr(NULL)
{}
Node::~Node()
{}

typedef map<Node*, Node*> NodeMap;

Node* GenerateNodelist(int count)
{
	if (count > 5) {
		return NULL;
	}
	Node* a = new Node();
	a->setLeftPtr(GenerateNodelist(count));
	a->setRightPtr(GenerateNodelist(count));
	return a;
}

Node* CopyNodelist(Node* cur, NodeMap& nodemap)
{
	if (cur == NULL) {
		return NULL;
	}
	NodeMap::iterator i = nodemap.find(cur);
	if (i != nodemap.end()) {
		return i->second;
	}
	Node* a = new Node();
	nodemap[cur] = a;
	a->setLeftPtr(CopyNodelist(cur->getLeftPtr(), nodemap));
	a->setRightPtr(CopyNodelist(cur->getRightPtr(), nodemap));
	return a;
}

int main(int argc, char* argv [])
{
	Node* root = GenerateNodelist(0);
	NodeMap nodemap;
	Node* copy_ptr = CopyNodelist(root, nodemap);
}
