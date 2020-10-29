"""Main module."""
from selenium import webdriver
from bs4 import BeautifulSoup
import re

class ElementFinder:
    
    def __init__(self, driver): 
        self.driver = driver
        
    def get_html_as_soup(self): 
        return BeautifulSoup(self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML"), "html.parser")

    def scroll_to_element(self, element):
        x = element.location['x']
        y = element.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        self.driver.execute_script(scroll_by_coord)
        self.driver.execute_script(scroll_nav_out_of_way)
    
    def find_elements_by_attribute_pattern(self, pattern, neg_pattern=None):    
        elements = self.search_soup_attributes(pattern, neg_pattern)
        xpaths = [self.get_element_xpath(elem) for elem in elements]
        selenium_elements = [self.driver.find_element_by_xpath(xpath) for xpath in xpaths]
        return selenium_elements
    
    def find_elements_by_text_search(self, pattern, neg_pattern, max_len): 
        elements = self.search_soup_text(pattern, neg_pattern, max_len)
        xpaths = [self.get_element_xpath(elem) for elem in elements]
        selenium_elements = [self.driver.find_element_by_xpath(xpath) for xpath in xpaths]
        return selenium_elements

    def get_element_xpath(self,element):
        components = []
        current = element if element.name else element.parent
        for parent in current.parents:  # type: bs4.element.Tag
            siblings = parent.find_all(current.name, recursive=False)
            
            if 1 == len(siblings):
                node = current.name
            else: 
                number = siblings.index(current) + 1
                node = "{name}[{number}]".format(name=current.name, number = number)
            components.append(node)
            current = parent
        
        if len(components): 
            if components[-1] != "html":
                components.append("html")
        
            components.append('')
        components.reverse()
        xpath = "/".join(components)
        return xpath
        
    def search_attributes_and_vals_for_pattern(self, tag, pattern):
        compiled_pattern = re.compile(pattern, flags=re.IGNORECASE)

        for k,v in tag.attrs.items():
            try:
                if compiled_pattern.search(k):
                    return True
                if type(v)=="list":
                    if compiled_pattern.search(' '.join(v)):
                        return True
                else: 
                    if compiled_pattern.search(str(v)):
                        return True
            except Exception as e:
                print(e)
        return False

    def apply_regex_to_attribute(self, tag, pattern, neg_pattern):
        #set_trace()
        if neg_pattern:
            if self.search_attributes_and_vals_for_pattern(tag, neg_pattern):
                return False
        
        return self.search_attributes_and_vals_for_pattern(tag, pattern)

    def search_soup_attributes(self, pattern, neg_pattern=None):
        soup = self.get_html_as_soup()
        return soup.find_all(lambda x: self.apply_regex_to_attribute(x, pattern, neg_pattern))
        
        
    def search_soup_text(self, pattern, neg_pattern, max_len=100):
        soup = self.get_html_as_soup()
        return soup.find_all(lambda x: self.get_tags_with_matching_text(x, pattern, neg_pattern, max_len))
                
    def get_tags_with_matching_text(self, tag, pattern, neg_pattern, max_len): 
        compiled_pattern = re.compile(pattern, flags = re.IGNORECASE)
        if len(tag.text) < 100:
            if compiled_pattern.search(tag.text):
                if neg_pattern:
                    compiled_neg_pattern = re.compile(pattern, flags = re.IGNORECASE)
                    return compiled_neg_pattern.search(tag.text)
                else:
                    return True
                
        

