from mrename.detection import get_handler
import mrename.handlers as handler

def test_handler_se_without_space():
    assert get_handler("asddsasda S1E03.mkv") is handler.rename_se
    assert get_handler("S101.mkv") is not handler.rename_se
    assert get_handler("S1xE01.mkv") is not handler.rename_se
    assert get_handler("S1E01") is not handler.rename_se
    assert get_handler("S1.mkv") is not handler.rename_se
    assert get_handler("E1.mkv") is not handler.rename_se
    assert get_handler("S1E.mkv") is not handler.rename_se
    assert get_handler("SE1.mkv") is not handler.rename_se

def test_handler_sxe_without_space():
    assert get_handler("S1xE01.mkv") is handler.rename_sxe
    assert get_handler("S1x01.mkv") is not handler.rename_sxe
    assert get_handler("S1E01.mkv") is not handler.rename_sxe
    assert get_handler("S1xE01") is not handler.rename_sxe
    assert get_handler("S1x.mkv") is not handler.rename_sxe
    assert get_handler("xE1.mkv") is not handler.rename_sxe
    assert get_handler("S1xE.mkv") is not handler.rename_sxe
    assert get_handler("SxE1.mkv") is not handler.rename_sxe

def test_handler_sde_without_space():
    assert get_handler("S1-E01.mkv") is handler.rename_sde
    assert get_handler("S1-01.mkv") is not handler.rename_sde
    assert get_handler("S1E01.mkv") is not handler.rename_sde
    assert get_handler("S1-E01") is not handler.rename_sde
    assert get_handler("S1-.mkv") is not handler.rename_sde
    assert get_handler("-E1.mkv") is not handler.rename_sde
    assert get_handler("S1-E.mkv") is not handler.rename_sde
    assert get_handler("S-E1.mkv") is not handler.rename_sde

def test_handler_x_without_space():
    assert get_handler("1x01.mkv") is handler.rename_x
    assert get_handler("S1x01.mkv") is not handler.rename_x
    assert get_handler("S1E01.mkv") is not handler.rename_x
    assert get_handler("1x01") is not handler.rename_x
    assert get_handler("1x.mkv") is not handler.rename_x
    assert get_handler("x1.mkv") is not handler.rename_x

def test_handler_e():
    assert get_handler("E01.mkv") is handler.rename_e
    assert get_handler("01.mkv") is not handler.rename_e
    assert get_handler("S1E01.mkv") is not handler.rename_e

def test_handler_num():
    assert get_handler("01.mkv") is handler.rename_num
    assert get_handler("S1E01.mkv") is not handler.rename_num
