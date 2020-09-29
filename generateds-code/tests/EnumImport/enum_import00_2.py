## #!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py.
# Python 3.8.3 (default, Jul  2 2020, 16:21:59)  [GCC 7.3.0]
#
# Command line options:
#   ('--disable-generatedssuper-lookup', '')
#   ('--disable-xml', '')
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--silence', '')
#   ('--member-specs', 'dict')
#   ('-f', '')
#   ('--one-file-per-xsd', '')
#   ('--output-directory', 'tests/EnumImport')
#   ('--use-source-file-as-module-name', '')
#
# Command line arguments:
#   tests/enum_import00.xsd
#
# Command line:
#   generateDS.py --disable-generatedssuper-lookup --disable-xml --no-dates --no-versions --silence --member-specs="dict" -f --one-file-per-xsd --output-directory="tests/EnumImport" --use-source-file-as-module-name tests/enum_import00.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
## try:
##     from lxml import etree as etree_
## except ImportError:
##     from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


## def parsexml_(infile, parser=None, **kwargs):
##     if parser is None:
##         # Use the lxml ElementTree compatible parser so that, e.g.,
##         #   we ignore comments.
##         try:
##             parser = etree_.ETCompatXMLParser()
##         except AttributeError:
##             # fallback to xml.etree
##             parser = etree_.XMLParser()
##     try:
##         if isinstance(infile, os.PathLike):
##             infile = os.path.join(infile)
##     except AttributeError:
##         pass
##     doc = etree_.parse(infile, parser=parser, **kwargs)
##     return doc

## def parsexmlstring_(instring, parser=None, **kwargs):
##     if parser is None:
##         # Use the lxml ElementTree compatible parser so that, e.g.,
##         #   we ignore comments.
##         try:
##             parser = etree_.ETCompatXMLParser()
##         except AttributeError:
##             # fallback to xml.etree
##             parser = etree_.XMLParser()
##     element = etree_.fromstring(instring, parser=parser, **kwargs)
##     return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.


class GeneratedsSuper(object):
    __hash__ = object.__hash__
    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
    class _FixedOffsetTZ(datetime_.tzinfo):
        def __init__(self, offset, name):
            self.__offset = datetime_.timedelta(minutes=offset)
            self.__name = name
        def utcoffset(self, dt):
            return self.__offset
        def tzname(self, dt):
            return self.__name
        def dst(self, dt):
            return None
    def gds_format_string(self, input_data, input_name=''):
        return input_data
    def gds_parse_string(self, input_data, node=None, input_name=''):
        return input_data
    def gds_validate_string(self, input_data, node=None, input_name=''):
        if not input_data:
            return ''
        else:
            return input_data
    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data)
    def gds_validate_base64(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data
    def gds_parse_integer(self, input_data, node=None, input_name=''):
        try:
            ival = int(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires integer value: %s' % exp)
        return ival
    def gds_validate_integer(self, input_data, node=None, input_name=''):
        try:
            value = int(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires integer value')
        return value
    def gds_format_integer_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_integer_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                int(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of integer valuess')
        return values
    def gds_format_float(self, input_data, input_name=''):
        return ('%.15f' % input_data).rstrip('0')
    def gds_parse_float(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires float or double value: %s' % exp)
        return fval_
    def gds_validate_float(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires float value')
        return value
    def gds_format_float_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_float_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of float values')
        return values
    def gds_format_decimal(self, input_data, input_name=''):
        return_value = '%s' % input_data
        if '.' in return_value:
            return_value = return_value.rstrip('0')
            if return_value.endswith('.'):
                return_value = return_value.rstrip('.')
        return return_value
    def gds_parse_decimal(self, input_data, node=None, input_name=''):
        try:
            decimal_value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return decimal_value
    def gds_validate_decimal(self, input_data, node=None, input_name=''):
        try:
            value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return value
    def gds_format_decimal_list(self, input_data, input_name=''):
        return ' '.join([self.gds_format_decimal(item) for item in input_data])
    def gds_validate_decimal_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                decimal_.Decimal(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of decimal values')
        return values
    def gds_format_double(self, input_data, input_name=''):
        return '%e' % input_data
    def gds_parse_double(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires double or float value: %s' % exp)
        return fval_
    def gds_validate_double(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires double or float value')
        return value
    def gds_format_double_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_double_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(
                    node, 'Requires sequence of double or float values')
        return values
    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()
    def gds_parse_boolean(self, input_data, node=None, input_name=''):
        if input_data in ('true', '1'):
            bval = True
        elif input_data in ('false', '0'):
            bval = False
        else:
            raise_parse_error(node, 'Requires boolean value')
        return bval
    def gds_validate_boolean(self, input_data, node=None, input_name=''):
        if input_data not in (True, 1, False, 0, ):
            raise_parse_error(
                node,
                'Requires boolean value '
                '(one of True, 1, False, 0)')
        return input_data
    def gds_format_boolean_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_boolean_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires sequence of boolean values '
                    '(one of True, 1, False, 0)')
        return values
    def gds_validate_datetime(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_datetime(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    @classmethod
    def gds_parse_datetime(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        time_parts = input_data.split('.')
        if len(time_parts) > 1:
            micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
            input_data = '%s.%s' % (
                time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt
    def gds_validate_date(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_date(self, input_data, input_name=''):
        _svalue = '%04d-%02d-%02d' % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(
                            hours, minutes)
        except AttributeError:
            pass
        return _svalue
    @classmethod
    def gds_parse_date(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
        dt = dt.replace(tzinfo=tz)
        return dt.date()
    def gds_validate_time(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_time(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%02d:%02d:%02d' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%02d:%02d:%02d.%s' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    def gds_validate_simple_patterns(self, patterns, target):
        # pat is a list of lists of strings/patterns.
        # The target value must match at least one of the patterns
        # in order for the test to succeed.
        found1 = True
        for patterns1 in patterns:
            found2 = False
            for patterns2 in patterns1:
                mo = re_.search(patterns2, target)
                if mo is not None and len(mo.group(0)) == len(target):
                    found2 = True
                    break
            if not found2:
                found1 = False
                break
        return found1
    @classmethod
    def gds_parse_time(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt.time()
    def gds_check_cardinality_(
            self, value, input_name,
            min_occurs=0, max_occurs=1, required=None):
        if value is None:
            length = 0
        elif isinstance(value, list):
            length = len(value)
        else:
            length = 1
        if required is not None :
            if required and length < 1:
                self.gds_collector_.add_message(
                    "Required value {}{} is missing".format(
                        input_name, self.gds_get_node_lineno_()))
        if length < min_occurs:
            self.gds_collector_.add_message(
                "Number of values for {}{} is below "
                "the minimum allowed, "
                "expected at least {}, found {}".format(
                    input_name, self.gds_get_node_lineno_(),
                    min_occurs, length))
        elif length > max_occurs:
            self.gds_collector_.add_message(
                "Number of values for {}{} is above "
                "the maximum allowed, "
                "expected at most {}, found {}".format(
                    input_name, self.gds_get_node_lineno_(),
                    max_occurs, length))
    def gds_validate_builtin_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value, input_name=input_name)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_validate_defined_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_str_lower(self, instring):
        return instring.lower()
    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path
    Tag_strip_pattern_ = re_.compile(r'\{.*\}')
    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)
    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1
    def gds_build_any(self, node, type_name=None):
        # provide default value in case option --disable-xml is used.
        content = ""
##         content = etree_.tostring(node, encoding="unicode")
        return content
    @classmethod
    def gds_reverse_node_mapping(cls, mapping):
        return dict(((v, k) for k, v in mapping.items()))
    @staticmethod
    def gds_encode(instring):
        if sys.version_info.major == 2:
            if ExternalEncoding:
                encoding = ExternalEncoding
            else:
                encoding = 'utf-8'
            return instring.encode(encoding)
        else:
            return instring
    @staticmethod
    def convert_unicode(instring):
        if isinstance(instring, str):
            result = quote_xml(instring)
        elif sys.version_info.major == 2 and isinstance(instring, unicode):
            result = quote_xml(instring).encode('utf8')
        else:
            result = GeneratedsSuper.gds_encode(str(instring))
        return result
    def __eq__(self, other):
        def excl_select_objs_(obj):
            return (obj[0] != 'parent_object_' and
                    obj[0] != 'gds_collector_')
        if type(self) != type(other):
            return False
        return all(x == y for x, y in zip_longest(
            filter(excl_select_objs_, self.__dict__.items()),
            filter(excl_select_objs_, other.__dict__.items())))
    def __ne__(self, other):
        return not self.__eq__(other)
    # Django ETL transform hooks.
    def gds_djo_etl_transform(self):
        pass
    def gds_djo_etl_transform_db_obj(self, dbobj):
        pass
    # SQLAlchemy ETL transform hooks.
    def gds_sqa_etl_transform(self):
        return 0, None
    def gds_sqa_etl_transform_db_obj(self, dbobj):
        pass
    def gds_get_node_lineno_(self):
        if (hasattr(self, "gds_elementtree_node_") and
                self.gds_elementtree_node_ is not None):
            return ' near line {}'.format(
                self.gds_elementtree_node_.sourceline)
        else:
            return ""


def getSubclassFromModule_(module, class_):
    '''Get the subclass of a class from a specific module.'''
    name = class_.__name__ + 'Sub'
    if hasattr(module, name):
        return getattr(module, name)
    else:
        return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
##     def export(self, outfile, level, name, namespace,
##                pretty_print=True):
##         if self.category == MixedContainer.CategoryText:
##             # Prevent exporting empty content as empty lines.
##             if self.value.strip():
##                 outfile.write(self.value)
##         elif self.category == MixedContainer.CategorySimple:
##             self.exportSimple(outfile, level, name)
##         else:    # category == MixedContainer.CategoryComplex
##             self.value.export(
##                 outfile, level, namespace, name_=name,
##                 pretty_print=pretty_print)
##     def exportSimple(self, outfile, level, name):
##         if self.content_type == MixedContainer.TypeString:
##             outfile.write('<%s>%s</%s>' % (
##                 self.name, self.value, self.name))
##         elif self.content_type == MixedContainer.TypeInteger or \
##                 self.content_type == MixedContainer.TypeBoolean:
##             outfile.write('<%s>%d</%s>' % (
##                 self.name, self.value, self.name))
##         elif self.content_type == MixedContainer.TypeFloat or \
##                 self.content_type == MixedContainer.TypeDecimal:
##             outfile.write('<%s>%f</%s>' % (
##                 self.name, self.value, self.name))
##         elif self.content_type == MixedContainer.TypeDouble:
##             outfile.write('<%s>%g</%s>' % (
##                 self.name, self.value, self.name))
##         elif self.content_type == MixedContainer.TypeBase64:
##             outfile.write('<%s>%s</%s>' % (
##                 self.name,
##                 base64.b64encode(self.value),
##                 self.name))
##     def to_etree(self, element, mapping_=None, nsmap_=None):
##         if self.category == MixedContainer.CategoryText:
##             # Prevent exporting empty content as empty lines.
##             if self.value.strip():
##                 if len(element) > 0:
##                     if element[-1].tail is None:
##                         element[-1].tail = self.value
##                     else:
##                         element[-1].tail += self.value
##                 else:
##                     if element.text is None:
##                         element.text = self.value
##                     else:
##                         element.text += self.value
##         elif self.category == MixedContainer.CategorySimple:
##             subelement = etree_.SubElement(
##                 element, '%s' % self.name)
##             subelement.text = self.to_etree_simple()
##         else:    # category == MixedContainer.CategoryComplex
##             self.value.to_etree(element)
##     def to_etree_simple(self, mapping_=None, nsmap_=None):
##         if self.content_type == MixedContainer.TypeString:
##             text = self.value
##         elif (self.content_type == MixedContainer.TypeInteger or
##                 self.content_type == MixedContainer.TypeBoolean):
##             text = '%d' % self.value
##         elif (self.content_type == MixedContainer.TypeFloat or
##                 self.content_type == MixedContainer.TypeDecimal):
##             text = '%f' % self.value
##         elif self.content_type == MixedContainer.TypeDouble:
##             text = '%g' % self.value
##         elif self.content_type == MixedContainer.TypeBase64:
##             text = '%s' % base64.b64encode(self.value)
##         return text
##     def exportLiteral(self, outfile, level, name):
##         if self.category == MixedContainer.CategoryText:
##             showIndent(outfile, level)
##             outfile.write(
##                 'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
##                     self.category, self.content_type,
##                     self.name, self.value))
##         elif self.category == MixedContainer.CategorySimple:
##             showIndent(outfile, level)
##             outfile.write(
##                 'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
##                     self.category, self.content_type,
##                     self.name, self.value))
##         else:    # category == MixedContainer.CategoryComplex
##             showIndent(outfile, level)
##             outfile.write(
##                 'model_.MixedContainer(%d, %d, "%s",\n' % (
##                     self.category, self.content_type, self.name,))
##             self.value.exportLiteral(outfile, level + 1)
##             showIndent(outfile, level)
##             outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

from .enum_import01 import Type01_1
from .enum_import02 import Type02_1

class EnumType00_1(str, Enum):
    """Simple type enumeration with restrictions"""
    FLOAT='float' # Enumeration value: 'float'
    INT='int' # Enumeration value: 'int'
    NAME='Name' # Enumeration value: 'Name'
    TOKEN='token' # Enumeration value: 'token'


class Type00_1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'inner01': MemberSpec_('inner01', 'Type01_1', 0, 0, {'name': 'inner01', 'type': 'Type01_1'}, None),
        'inner02': MemberSpec_('inner02', 'Type02_1', 0, 0, {'name': 'inner02', 'type': 'Type02_1'}, None),
    }
    subclass = None
    superclass = None
    def __init__(self, inner01=None, inner02=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.inner01 = inner01
        self.inner02 = inner02
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Type00_1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Type00_1.subclass:
            return Type00_1.subclass(*args_, **kwargs_)
        else:
            return Type00_1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_inner01(self):
        return self.inner01
    def set_inner01(self, inner01):
        self.inner01 = inner01
    def get_inner02(self):
        return self.inner02
    def set_inner02(self, inner02):
        self.inner02 = inner02
    def hasContent_(self):
        if (
            self.inner01 is not None or
            self.inner02 is not None
        ):
            return True
        else:
            return False
# end class Type00_1


class Type00_2(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'attr1': MemberSpec_('attr1', 'enum_import01:IntType01_1', 0, 1, {'use': 'optional'}),
    }
    subclass = None
    superclass = None
    def __init__(self, attr1='33', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.attr1 = _cast(int, attr1)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Type00_2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Type00_2.subclass:
            return Type00_2.subclass(*args_, **kwargs_)
        else:
            return Type00_2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_attr1(self):
        return self.attr1
    def set_attr1(self, attr1):
        self.attr1 = attr1
    def validate_IntType01_1(self, value):
        # Validate type enum_import01:IntType01_1, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on IntType01_1' % {"value": value, "lineno": lineno} )
                result = False
            if value > 127:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on IntType01_1' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
# end class Type00_2


GDSClassesMapping = {
}


RenameMappings_ = {

}
__all__ = [
    "Type00_1",
    "Type00_2",
    "Type01_1",
    "Type02_1"
]
