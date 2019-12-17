# KInterbasDB Python Package - Type Conv : Text/Unicode
#
# Version 3.3
#
# The following contributors hold Copyright (C) over their respective
# portions of code (see license.txt for details):
#
# [Original Author (maintained through version 2.0-0.3.1):]
#   1998-2001 [alex]  Alexander Kuznetsov   <alexan@users.sourceforge.net>
# [Maintainers (after version 2.0-0.3.1):]
#   2001-2002 [maz]   Marek Isalski         <kinterbasdb@maz.nu>
#   2002-2006 [dsr]   David Rushby          <woodsplitter@rocketmail.com>
# [Contributors:]
#   2001      [eac]   Evgeny A. Cherkashin  <eugeneai@icc.ru>
#   2001-2002 [janez] Janez Jere            <janez.jere@void.si>

__all__ = (
    'unicode_conv_in', 'unicode_conv_out', 'DB_TO_PYTHON_ENCODING_MAP',
  )

import sys
from kinterbasdb.k_exceptions import *

# The database character set codes (the *keys* in DB_TO_PYTHON_ENCODING_MAP)
# are defined on pages 221-225 of the Interbase 6 Data Definition Guide.
# The Python codec names (the *values* in DB_TO_PYTHON_ENCODING_MAP) are
# defined in section 4.9.2 "Standard Encodings" of the Python Library
# Reference.
#
# The character sets supported by a given database can be determined with the
# following query:
#   select rdb$character_set_id, rdb$character_set_name
#   from rdb$character_sets order by rdb$character_set_id

DB_TO_PYTHON_ENCODING_MAP = {
  # The following three database character set codes are not handled by
  # kinterbasdb's TEXT_UNICODE dynamic type translation (they're handled by
  # TEXT instead, and deal with plain Python strings):
  #  0 -> 'NONE'
  #  1 -> 'OCTETS'
  #  2 -> 'ASCII'

  # DB CODE  : PYTHON NAME          : DB NAME
  # ---------------------------------------------------------------------------
            3: 'utf_8',            #: 'UNICODE_FSS'
            4: 'utf_8',            #: 'UTF8' (Firebird 2.0+)
            5: 'shift_jis',        #: 'SJIS_0208'
            6: 'euc_jp',           #: 'EUCJ_0208'
            9: 'cp737',            #: 'DOS737'
           10: 'cp437',            #: 'DOS437'
           11: 'cp850',            #: 'DOS850'
           12: 'cp865',            #: 'DOS865'
           13: 'cp860',            #: 'DOS860'
           14: 'cp863',            #: 'DOS863'
           15: 'cp775',            #: 'DOS775'
         # 16: NOT SUPPORTED,      #: 'DOS858'
           17: 'cp862',            #: 'DOS862'
           18: 'cp864',            #: 'DOS864'
         # 19: NOT SUPPORTED,      #: 'NEXT'
           21: 'iso8859_1',        #: 'ISO8859_1'
           22: 'iso8859_2',        #: 'ISO8859_2'
           23: 'iso8859_3',        #: 'ISO8859_3'
           34: 'iso8859_4',        #: 'ISO8859_4'
           35: 'iso8859_5',        #: 'ISO8859_5'
           36: 'iso8859_6',        #: 'ISO8859_6'
           37: 'iso8859_7',        #: 'ISO8859_7'
           38: 'iso8859_8',        #: 'ISO8859_8'
           39: 'iso8859_9',        #: 'ISO8859_9'
           40: 'iso8859_13',       #: 'ISO8859_13'
           44: 'euc_kr',           #: 'KSC_5601'
           45: 'cp852',            #: 'DOS852'
           46: 'cp857',            #: 'DOS857'
           47: 'cp861',            #: 'DOS861'
           48: 'cp866',            #: 'DOS866'
           49: 'cp869',            #: 'DOS869'
         # 50: NOT SUPPORTED,      #: 'CYRL'
           51: 'cp1250',           #: 'WIN1250'
           52: 'cp1251',           #: 'WIN1251'
           53: 'cp1252',           #: 'WIN1252'
           54: 'cp1253',           #: 'WIN1253'
           55: 'cp1254',           #: 'WIN1254'
           56: 'big5',             #: 'BIG_5'
           57: 'gb2312',           #: 'GB_2312'
           58: 'cp1255',           #: 'WIN1255'
           59: 'cp1256',           #: 'WIN1256'
           60: 'cp1257',           #: 'WIN1257'
           63: 'koi8_r',           #: 'KOI8-R' (Firebird 2.0+)
           64: 'koi8_u',           #: 'KOI8-U' (Firebird 2.0+)
           65: 'cp1258',           #: 'WIN1258' (Firebird 2.0+)
  }

DB_CHAR_SET_NAME_TO_PYTHON_ENCODING_MAP = {
    # DB CHAR SET NAME    :   PYTHON CODEC NAME (CANONICAL)
    # ---------------------------------------------------------------------------
    'OCTETS'              :   None, # Allow to pass through unchanged.
    'UNICODE_FSS'         :   'utf_8',
    'UTF8'                :   'utf_8', # (Firebird 2.0+)
    'SJIS_0208'           :   'shift_jis',
    'EUCJ_0208'           :   'euc_jp',
    'DOS737'              :   'cp737',
    'DOS437'              :   'cp437',
    'DOS850'              :   'cp850',
    'DOS865'              :   'cp865',
    'DOS860'              :   'cp860',
    'DOS863'              :   'cp863',
    'DOS775'              :   'cp775',
    'DOS862'              :   'cp862',
    'DOS864'              :   'cp864',
    'ISO8859_1'           :   'iso8859_1',
    'ISO8859_2'           :   'iso8859_2',
    'ISO8859_3'           :   'iso8859_3',
    'ISO8859_4'           :   'iso8859_4',
    'ISO8859_5'           :   'iso8859_5',
    'ISO8859_6'           :   'iso8859_6',
    'ISO8859_7'           :   'iso8859_7',
    'ISO8859_8'           :   'iso8859_8',
    'ISO8859_9'           :   'iso8859_9',
    'ISO8859_13'          :   'iso8859_13',
    'KSC_5601'            :   'euc_kr',
    'DOS852'              :   'cp852',
    'DOS857'              :   'cp857',
    'DOS861'              :   'cp861',
    'DOS866'              :   'cp866',
    'DOS869'              :   'cp869',
    'WIN1250'             :   'cp1250',
    'WIN1251'             :   'cp1251',
    'WIN1252'             :   'cp1252',
    'WIN1253'             :   'cp1253',
    'WIN1254'             :   'cp1254',
    'BIG_5'               :   'big5',
    'GB_2312'             :   'gb2312',
    'WIN1255'             :   'cp1255',
    'WIN1256'             :   'cp1256',
    'WIN1257'             :   'cp1257',
    'KOI8-R'              :   'koi8_r', # (Firebird 2.0+)
    'KOI8-U'              :   'koi8_u', # (Firebird 2.0+)
    'WIN1258'             :   'cp1258', # (Firebird 2.0+)
  }

# The inverse of DB_CHAR_SET_NAME_TO_PYTHON_ENCODING_MAP:
PYTHON_ENCODING_TO_DB_CHAR_SET_NAME_MAP = dict(
        (val, key)
    for (key, val)
    in DB_CHAR_SET_NAME_TO_PYTHON_ENCODING_MAP.iteritems()
  )

DB_CHAR_SET_NAME_TO_DB_CHAR_SET_ID_MAP = {} # Example entry: 'WIN1251': 52
for dbCharSetID, pythonEncodingName in DB_TO_PYTHON_ENCODING_MAP.iteritems():
    dbCharSetName = PYTHON_ENCODING_TO_DB_CHAR_SET_NAME_MAP[pythonEncodingName]
    DB_CHAR_SET_NAME_TO_DB_CHAR_SET_ID_MAP[dbCharSetName] = dbCharSetID
del dbCharSetID, pythonEncodingName, dbCharSetName


_UNKNOWN_CHARSET_MSG = (
    "Don't know how to %s value %s charset with numeric ID %d."
    " If you are using an unofficial character set, you should add a"
    " corresponding entry to kinterbasdb's translation table, as in:\n"
    "  kinterbasdb.typeconv_text_unicode.DB_TO_PYTHON_ENCODING_MAP[%d] = 'XX'\n"
    "where XX is the name of a Python codec."
    " Standard Python codecs are listed in section 4.9.2 ('Standard"
    " Encodings') of the Python documentation."
  )


def unicode_conv_in((unicodeString, dbCharacterSetCode)):
    if unicodeString is None:
        return None

    # Modulate dbCharacterSetCode by 256 to get rid of collation info.
    dbCharacterSetCode %= 256

    pyEncodingName = DB_TO_PYTHON_ENCODING_MAP.get(dbCharacterSetCode, None)
    if pyEncodingName is not None:
        return unicodeString.encode(pyEncodingName)
    else:
        raise OperationalError( _UNKNOWN_CHARSET_MSG % (
            'encode', 'to', dbCharacterSetCode, dbCharacterSetCode
          ))


def unicode_conv_out((rawString, dbCharacterSetCode)):
    if rawString is None:
        return None

    # Modulate dbCharacterSetCode by 256 to get rid of collation info.
    dbCharacterSetCode %= 256

    pyEncodingName = DB_TO_PYTHON_ENCODING_MAP.get(dbCharacterSetCode, None)
    if pyEncodingName is not None:
        return rawString.decode(pyEncodingName)
    else:
        raise OperationalError( _UNKNOWN_CHARSET_MSG % (
            'decode', 'from', dbCharacterSetCode, dbCharacterSetCode
          ))
