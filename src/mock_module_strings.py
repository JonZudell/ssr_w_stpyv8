_element = """
var __element = function() {
  return {
    nodeType: 1,
    nodeName: 'DIV',
    hasChildNodes: function() {
      return this.childNodes && this.childNodes.length > 0;
    },
    appendChild: function(child) {
      if (!this.childNodes) {
        this.childNodes = [];
      }
      this.childNodes.push(child);
      console.log('appendChild called');
    },
    removeChild: function(child) {
      if (this.childNodes) {
        var index = this.childNodes.indexOf(child);
        if (index > -1) {
          this.childNodes.splice(index, 1);
          console.log('removeChild called');
        }
      }
    },
    setAttribute: function(name, value) {
      if (!this.attributes) {
        this.attributes = {};
      }
      this.attributes[name] = value;
      console.log('setAttribute called with', name, value);
    },
    getAttribute: function(name) {
      if (this.attributes && this.attributes[name]) {
        console.log('getAttribute called with', name);
        return this.attributes[name];
      }
      return null;
    },
    addEventListener: function(type, listener) {
      console.log('addEventListener called with', type);
      if (!this[type]) {
        this[type] = [];
      }
      this[type].push(listener);
    },
    removeEventListener: function(type, listener) {
      console.log('removeEventListener called with', type);
      if (this[type]) {
        var index = this[type].indexOf(listener);
        if (index > -1) {
          this[type].splice(index, 1);
        }
      }
    },
    ownerDocument: document,
    style: {},
    innerHTML: '',
    innerText: '',
    textContent: '',
    childNodes: [],
    attributes: {}
  }
}
"""
_text_node = """
var __textNode = function() {
  return {
    textContent: '',
    nodeType: 3, // Node.TEXT_NODE
    ownerDocument: document
  }
}
"""

_comment_node = """
var __commentNode = function() {
  return {
    data: '',
    nodeType: 8, // Node.COMMENT_NODE
    ownerDocument: document
  }
}
"""

_document_fragment_node = """
var __documentFragment = function() {
  return {
    nodeType: 11, // Node.DOCUMENT_FRAGMENT_NODE
    ownerDocument: document,
    appendChild: function(child) {
      console.log('appendChild called');
    }
  }
}
"""
_document = """var document = {
  nodeType: 9,
  location: {
    href: 'http://localhost'
  },
  title: '',
  body: __element(),
  head: __element(),
  documentElement: __element(),
  getElementById: function(id) {
    console.log('document.getElementById called', id);
    return __element();
  },
  getElementsByClassName: function(className) {
    console.log('document.getElementsByClassName called', className);
    return [ __element()];
  },
  getElementsByTagName: function(tagName) {
    console.log('document.getElementsByTagName called', tagName);
    return [ __element()];
  },
  querySelector: function(selector) {
    console.log('document.querySelector called', selector);
    return  __element();
  },
  querySelectorAll: function(selector) {
    console.log('document.querySelectorAll called', selector);
    return [ __element()];
  },
  createElement: function(tag) {
    console.log('document.createElement called', tag);
    return  __element();
  },
  createTextNode: function(text) {
    var textNode = __textNode();
    textNode.textContext = text
    return textNode;
  },
  createComment: function(data) {
    var commentNode =  __commentNode();
    commentNode.data = data;
    return commentNode;
  },
  createDocumentFragment: function() {
    return __documentFragment();
  },
  write: function(text) {
  },
  addEventListener: function(type, listener) {
    console.log('addEventListener called with', type);
    if (!this[type]) {
      this[type] = [];
    }
    this[type].push(listener);
  },
  removeEventListener: function(type, listener) {
    console.log('removeEventListener called with', type);
    if (this[type]) {
      var index = this[type].indexOf(listener);
      if (index > -1) {
        this[type].splice(index, 1);
      }
    }
  },
  matchMedia: function(query) {
    return {
      matches: false,
      media: query,
      onchange: null,
      addListener: function(listener) {
        console.log('matchMedia.addListener called with', listener);
      },
      removeListener: function(listener) {
        console.log('matchMedia.removeListener called with', listener);
      }
    };
  },
};"""

_self = "var self = document;"
_global = """"""
_window = """var window = self;"""
_url = """var URL = function(url) {
  this.href = url;
};"""

_bootstrap = '\n'.join([_element, _comment_node, _document_fragment_node, _text_node, _document, _self, _global, _window, _url])