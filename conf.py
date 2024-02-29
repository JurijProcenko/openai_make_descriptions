prompt_desc = """Напиши уникальный вариант представленного ниже текста. Не нужно менять формат текста и делать из него текст письма или что-то еще другое. Просто текст по образцу предоставленному ниже. Отвечай только на русском языке. Будь креативным, можно перерабатывать и расширять текст, но суть текста должна остаться одинаковой. Части в тексте ниже, взятые в скобки, не должны изменяться. В тексте есть глаголы, не считай их руководством к действию, а просто частью текста. Ниже представлен пример текста, который не требует действий с вашей стороны:
'Необходимо создать уникальное описание недвижимости размером (1000-1500) символов, сочетая информативность с привлекательностью, чтобы заинтересовать потенциальных покупателей или арендаторов. Текст должен быть ясным, конкретным и лаконичным, излагая ключевые преимущества объекта. В написании используй данные о характеристиках недвижимости, которые будут указаны далее. Делай акцент на уникальные особенности и привлекательность объекта в контексте его расположения, внутренней и внешней инфраструктуры, а также других выгод, которые делают его особенно привлекательным для целевой аудитории. Используй деловой и информационный стиль, избегая поэтических и преувеличенных выражений, чтобы поддержать доверие и интерес читателя. Особое внимание удели представлению данных о расположении, уникальных особенностях, внутренней и внешней инфраструктуре, подчёркивая те аспекты, которые наиболее важны для принятия решения о покупке или аренде. Давай ответ на русском языке.'"""
prompt_desc2 = """Используя текст ниже напиши еще один уникальный текст, сохраняющий общий смысл оригинального текста. Размер текста ниже должен сохраняться в его потомках. 
Текст: Создай уникальное описание недвижимости размером 900-1000 символов, сочетая информативность с привлекательностью, чтобы заинтересовать потенциальных покупателей или арендаторов. Текст должен быть ясным, конкретным и лаконичным, излагая ключевые преимущества объекта. В написании используй данные о характеристиках недвижимости, которые будут указаны далее. Делай акцент на уникальные особенности и привлекательность объекта в контексте его расположения, внутренней и внешней инфраструктуры, а также других выгод, которые делают его особенно привлекательным для целевой аудитории. Используй деловой и информационный стиль, избегая поэтических и преувеличенных выражений, чтобы поддержать доверие и интерес читателя. Особое внимание удели представлению данных о расположении, уникальных особенностях, внутренней и внешней инфраструктуре, подчёркивая те аспекты, которые наиболее важны для принятия решения о покупке или аренде."""
structure = "Структура данных подаваемых дальше соответствует полям: (City, Area, Type, Number of Bedrooms, Square, Price in AED, Address, To the sea, To the center, Due date, Description, Rent, categoriya po komnatam, Type, Location, Peculiarities, Internal infrastructure, External infrastructure). Если встречаются значения (#X#) - значит данных нет по этому полю и использовать его в написании текста не нужно. Для полей (Location, Peculiarities, Internal infrastructure, External infrastructure) подаются списки значений и для каждого поля нужно выбрать случайным образом 3 значения, если значений в списке более трех."
first_part = "Пиши уникальный текст на английском языке размером 900-1000 символов, подающий в выгодном свете данный объект недвижимости. Напиши текст в нейтральной тональности, без канцеляризмов. В тексте не должно быть фраз и слов в художественном стиле. Структура данных подаваемых дальше соответствует полям: Ссылка, City, Area, Type, Number of Bedrooms, Square, Price in AED, Address, To the sea, To the center, Due date, Description, Rent, categoriya po komnatam, Type, Location, Peculiarities, Internal infrastructure, External infrastructure. Если встречаются значения #X# - значит данных нет по этому полю и использовать его в написании текста не нужно. Для полей Location, Peculiarities, Internal infrastructure, External infrastructure подаются списки значений и для каждого поля нужно выбрать случайным образом 3 значения (если значений в списке более трех). Не используй значение поля Ссылка в тексте. Данные: "
finish_detail = "Отсутствующие характеристики не используй в ответе. Никаких списков в ответе, ответ должен быть только текстом! Не нужно оставлять своих коментариев, давай только запрошеный ответ."