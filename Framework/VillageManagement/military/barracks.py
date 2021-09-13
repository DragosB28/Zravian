from Framework.VillageManagement.Utils import check_building_page_title
from Framework.VillageManagement.Builder import XPATH
from Framework.utils.Logger import get_projectLogger
from Framework.utils.Constants import  BuildingType, TroopType, get_TROOPS, get_XPATH
from Framework.utils.SeleniumUtils import clickElement, getElementAttribute, sendKeys
from Framework.screen.Views import TRIBE, getTribe

logger = get_projectLogger()
TRIBE = getTribe()
TROOPS = get_TROOPS()
XPATH = get_XPATH()

def make_troops_by_amount(driver, tpType, amount):
    """
    Trains Troops by specified type and amount.

    Parameters:
        - driver (WebDriver): Used to interact with the webpage.
        - tpType (TroopType): Denotes troop.
        - amount: Denotes the amount of troops to be trained.

    Returns:
        - True if the operation is successful, False otherwise.
    """
    status = False
    if isinstance(tpType, TroopType):
        if check_building_page_title(driver, BuildingType.Barracks):
            if getElementAttribute(driver, XPATH.TRAIN_TROOP_REQ % TROOPS[tpType].name, 999) > amount:
                if sendKeys(driver, XPATH.TRAIN_TROOP_TYPE % TROOPS[tpType].name, amount):
                    if clickElement(driver, XPATH.TRAIN_TROOP):
                        logger.success(f'In function make_troops_by_amount: {TROOPS[tpType].name} was researched')
                        status = True
                    else:
                        logger.error('In function make_troops_by_amount: Failed to press train')
                else:
                    logger.error('In function make_troops_by_amount: Failed to insert amount of troops')
            else:
                logger.error('In function make_troops_by_amount: Not enough resources')
        else:
            logger.error('In function make_troops_by_amount: Not barracks screen')
    else:
        logger.error('In function make_troops_by_amount: Invalid parameter tptype')
    return status

    