import json

class Recipe:

    NUTRIENT_TAG = './/ul[@class="nutrientLine"]'
    TIME_TAG = './/ul[@class="prepTime"]'
    GENERAL_TAG = './/section[contains(@class, "recipe-summary")]'
    RATING_TAG = './/div[@class="rating-stars"]'
    NUM_RATINGS_TAG = './/span[@class="review-count"]'
    DESCRIPTION_TAG = './/div[@class="submitter__description"]'
    CATEGORY_TAG = './/ul[@class="breadcrumbs breadcrumbs"]'
    SUBCATEGORY_TAG = './/span[@class="toggle-similar__title"]'
    INGREDIENTS_TAGS = ['.//ul[@class="checklist dropdownwrapper list-ingredients-1"]',
                        './/ul[@class="checklist dropdownwrapper list-ingredients-2"]']
    INGREDIENT_ID_TAG = './/input[@name="ingredientCheckbox"]'
    INGREDIENT_TAG = './/span[@itemprop="ingredients"]'
    INSTRUCTIONS_TAG = './/ol[@class="list-numbers recipe-directions__list"]'

    def __init__(self):
        self.properties = {}

    def parsePage(self, lxml_data, id):
        self.properties['id'] = id
        self.parseAttributes(lxml_data)
        #self.parseNutrition(lxml_data)
        self.parseIngredients(lxml_data)
       # self.parseInstructions(lxml_data)

    # We do not need the following function as I don't think it's an appropriate feature in our learning algorithm(s).#
    # def parseNutrition(self, lxml_data):
    #     nutrients = lxml_data.xpath(self.NUTRIENT_TAG)
    #     for nutrient in nutrients:
    #         values = nutrient.xpath('.//li')
    #         key = values[0].text.split(':', 1)[0]
    #         value = values[1].text_content().strip()
    #         self.properties[key] = value

    def parseIngredients(self, lxml_data):
        ingredients_blocks = []
        for tag in self.INGREDIENTS_TAGS:
            ingredients_blocks.append(lxml_data.xpath(tag)[0])
        ingredients_array = []
        for block in ingredients_blocks:
            for ingredient in block:
                ingredient_id = ingredient.xpath(self.INGREDIENT_ID_TAG)
                if ingredient_id:
                    # commented out the ingredient id, as I don't think it's needed as an actual feature #
                    #ingredient_id = ingredient_id[0].get("data-id").strip()
                    ingredient_str = ingredient.xpath(self.INGREDIENT_TAG)[0].text_content().strip()
                    #ingredients_array.append((ingredient_id, ingredient_str))
                    ingredients_array.append(ingredient_str)
        self.properties['ingredients'] = ingredients_array

    def parseAttributes(self, lxml_data):
        time_block = lxml_data.xpath(self.TIME_TAG)

        # commented out the prep time feature, as I don't think it's needed as an actual feature #
        # if len(time_block) > 0:
        #     time_block = time_block[0]
        #     time_types = time_block.xpath('.//p')
        #     times = time_block.xpath('.//time')
        #     for i in xrange(len(time_types)):
        #         self.properties[time_types[i].text_content().strip()] = times[i].text_content().strip()

        general_block = lxml_data.xpath(self.GENERAL_TAG)[0]
        self.properties['name'] = general_block.xpath('.//h1')[0].text_content().strip()
        self.properties['rating'] = float(general_block.xpath(self.RATING_TAG)[0].get("data-ratingstars").strip())
        self.properties['num_ratings'] = int(general_block.xpath(self.NUM_RATINGS_TAG)[0].text_content().strip().split(' ', 1)[0])
        self.properties['description'] = general_block.xpath(self.DESCRIPTION_TAG)[0].text_content().strip()

        category_block = lxml_data.xpath(self.CATEGORY_TAG)[0]
        categories = category_block.xpath(self.SUBCATEGORY_TAG)
        category_array = []
        for i in xrange(2, len(categories)):
            category_array.append(categories[i].text_content().strip())
        self.properties['categories'] = category_array

    # We do not need the following function as I don't think it's an appropriate feature in our learning algorithm(s).#
    # def parseInstructions(self, lxml_data):
    #     instructions_block = lxml_data.xpath(self.INSTRUCTIONS_TAG)[0]
    #     instructions = instructions_block.xpath('.//li')
    #     instructions_array = []
    #     for instruction in instructions:
    #         instructions_array.append(instruction.text_content().strip())
    #     self.properties['instructions'] = instructions_array

    def toJSON(self):
        return json.dumps(self.properties)
