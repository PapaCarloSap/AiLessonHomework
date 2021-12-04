from enum import Enum
import html
from typing import Iterable
import re
import hw1.text_utils as text_utils


class Language(Enum):
    En = 1033
    Ru = 1049

class TextTransformer:
    def __init__(self, language:Language):
        self.__language = language
        
    def __init__(self, converters_map:Iterable) -> None:
        self.__converters_map = converters_map
        
    def transform(self, text:str):
        result = text
        for action in self.__converters_map:
            result = action(result)
        return result
    
class TextEditor:
    def __init__(self, 
                 apostrophe_dict = text_utils.apostrophe_dict, 
                 short_word_dict = text_utils.short_word_dict, 
                 emoticon_dict = text_utils.emoticon_dict):
        self.__apostrophe_dict = apostrophe_dict
        self.__short_word_dict = short_word_dict
        self.__emoticon_dict = emoticon_dict
      
    def convert_html_symbol(self, text:str)->str:
        """Преобразование спецсимволов html в unicode
            `&copy;` 2013  -->  © 2013

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:            
            >>> convert_html_symbol('&copy; 2013')
            '© 2013'
        """
        return html.unescape(text)

    def remove_at_word(self, text:str)->str:
        """Удалить все слова начинающиеся на @ из текста

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:            
            >>> remove_at_word('aa1 @user aa1 aa1')
            'aa1 aa1 aa1'
        """
        return re.sub('@[\w]*[\s]?','',text).rstrip()
            
    def to_lower(self, text:str)->str:
        """Перевести в нижний регистр

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:            
            >>> to_lower('AaaAaa')
            'aaaaaa'
        """
        return text.lower()

    def change_apostrophe_word(self, text:str)->str:
        """Замена сокращения с апострофами на полные словосочетания

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> change_apostrophe_word("can\'t")
            'cannot'
        """
        return self.__change_word(text, self.__apostrophe_dict)
    
    def change_abbreviation_to_words(self, text:str)->str:
        """Замена абревиатур полные словосочетания

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> change_abbreviation_to_words("afk")
            'away from keyboard'
        """
        return self.__change_word(text, self.__short_word_dict)
    
    def change_emoticon_to_word(self, text:str)->str:
        """Замена эмотиконы на эмоцию

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> change_emoticon_to_word(':-)')
            'happy'
        """
        return self.__change_word(text, self.__emoticon_dict)
    
    def remove_punctuation(self, text:str)->str:
        """Удаление знаков пунктуации (замена на пробел)

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> remove_punctuation('aa, aa')
            'aa  aa'
        """
        return re.sub(r'[^\w\s]',' ',text)
    
    def remove_spec_symbol(self, text:str)->str:
        """Удаление спец. символов (замена на пробел)

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> remove_spec_symbol('aa$ aa')
            'aa  aa'
        """
        return re.sub(r'[^a-zA-Z0-9]',' ',text)
    
    def remove_numbers(self, text:str)->str:
        """Удаление чисел (замена на пробел)

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> remove_numbers('aa123 aa')
            'aa    aa'
        """
        return re.sub(r'[^a-zA-Z]',' ',text)
    
    def remove_word_with_len_one(self, text:str)->str:
        """Удаление слова длиной в 1 символ

        Args:
            text (str): перобразуемый текст

        Returns:
            str: результат
            
        Examples:
            >>> remove_word_with_len_one('aa123 a aa')
            'aa123 aa'
        """
        return  ' '.join([w for w in text.split() if len(w)>1])
        
    def __change_word(self, text:str, dict:dict)->str:
        result = list()
        for word in text.split():
            if word in dict:
                result.append(dict[word])
            else:
                result.append(word)
        return ' '.join(result)