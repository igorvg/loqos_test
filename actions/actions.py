import random
from typing import Dict, Text, Any, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionStartTextBtns(Action):

    def name(self) -> Text:
        return "action_start_text_btns"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #набор текстов для рандомного выбора
        responses = [
            "Напиши свой вопрос или выбери один из разделов.",
            "Кликни на нужный раздел или напиши вопрос.",
            "Выбери одну из кнопок или задай свой вопрос."
        ]

        text = random.choice(responses)
        button_type = "vertical"

        buttons=[
            {"payload": "/documents", "title": "Документы"},
            {"payload": "/company_setup", "title": "Открыть компанию"},
            {"payload": "/taxes", "title": "Налоги на Кипре"}
        ]

        dispatcher.utter_message(text=text, buttons=buttons, button_type=button_type)

        return []

class ActionDocumentsTextBtns(Action):

    def name(self) -> Text:
        return "action_documents_text_btns"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #набор текстов для рандомного выбора
        responses = [
            "Нажми на кнопку и узнай подробнее:",
            "Чтобы прочитать информацию, нажми на одну из кнопок:",
            "Выбери кнопку и узнай подробности:"
        ]

        text = random.choice(responses)
        button_type = "vertical"

        buttons=[
            {"payload": "/visas_entry", "title": "Визы для въезда"},
            {"payload": "/police_certificate", "title": "Справка о несудимости"},
            {"payload": "/documents_translation", "title": "Перевод документов"},
            {"payload": "/other_question", "title": "Другой вопрос"}
        ]

        dispatcher.utter_message(text=text, buttons=buttons, button_type=button_type)

        return []
    
class ActionCompanySetOption(Action):

    def name(self) -> Text:
        return "action_company_set_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получаем значение слота из сущности 'company_choice'
        company_choice = tracker.get_slot("company_choice")

        # Обрабатываем вариант
        if company_choice == "types":
            response = "Вы выбрали тему: Типы компаний"
        elif company_choice == "setup":
            response = "Вы выбрали тему: Зарегистрировать компанию"
        else: 
            response = "Вы выбрали тему: Обязательства и платежи"

        
        buttons= [
            {"payload": "/thanks", "title": "Спасибо"},
            {"payload": "/company_setup", "title": "Назад"},
        ]

        dispatcher.utter_message(text=response, buttons=buttons)

        return []
    
class ActionTaxesSetOption(Action):

    def name(self) -> Text:
        return "action_taxes_set_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Получаем значение слота из сущности 'taxes_choice'
        taxes_choice = tracker.get_slot("taxes_choice")

        # Обрабатываем вариант
        if taxes_choice == "residention":
            response = "Вы выбрали тему: Стать налоговым резидентом Кипра"
        elif taxes_choice == "calculator":
            response = "Вы выбрали тему: Калькулятор налогообложения"
        else: 
            response = "Вы выбрали тему: Индивидуальное налогообложение"

        
        buttons= [
            {"payload": "/thanks", "title": "Спасибо"},
            {"payload": "/taxes", "title": "Назад"},
        ]

        dispatcher.utter_message(text=response, buttons=buttons)

        return []