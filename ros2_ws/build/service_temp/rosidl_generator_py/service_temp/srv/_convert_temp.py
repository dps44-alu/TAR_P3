# generated from rosidl_generator_py/resource/_idl.py.em
# with input from service_temp:srv/ConvertTemp.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ConvertTemp_Request(type):
    """Metaclass of message 'ConvertTemp_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('service_temp')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'service_temp.srv.ConvertTemp_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__convert_temp__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__convert_temp__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__convert_temp__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__convert_temp__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__convert_temp__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ConvertTemp_Request(metaclass=Metaclass_ConvertTemp_Request):
    """Message class 'ConvertTemp_Request'."""

    __slots__ = [
        '_input_temp',
        '_conversion_type',
    ]

    _fields_and_field_types = {
        'input_temp': 'double',
        'conversion_type': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.input_temp = kwargs.get('input_temp', float())
        self.conversion_type = kwargs.get('conversion_type', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.input_temp != other.input_temp:
            return False
        if self.conversion_type != other.conversion_type:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def input_temp(self):
        """Message field 'input_temp'."""
        return self._input_temp

    @input_temp.setter
    def input_temp(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'input_temp' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'input_temp' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._input_temp = value

    @builtins.property
    def conversion_type(self):
        """Message field 'conversion_type'."""
        return self._conversion_type

    @conversion_type.setter
    def conversion_type(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'conversion_type' field must be of type 'str'"
        self._conversion_type = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_ConvertTemp_Response(type):
    """Metaclass of message 'ConvertTemp_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('service_temp')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'service_temp.srv.ConvertTemp_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__convert_temp__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__convert_temp__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__convert_temp__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__convert_temp__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__convert_temp__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ConvertTemp_Response(metaclass=Metaclass_ConvertTemp_Response):
    """Message class 'ConvertTemp_Response'."""

    __slots__ = [
        '_converted_temp',
    ]

    _fields_and_field_types = {
        'converted_temp': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.converted_temp = kwargs.get('converted_temp', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.converted_temp != other.converted_temp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def converted_temp(self):
        """Message field 'converted_temp'."""
        return self._converted_temp

    @converted_temp.setter
    def converted_temp(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'converted_temp' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'converted_temp' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._converted_temp = value


class Metaclass_ConvertTemp(type):
    """Metaclass of service 'ConvertTemp'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('service_temp')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'service_temp.srv.ConvertTemp')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__convert_temp

            from service_temp.srv import _convert_temp
            if _convert_temp.Metaclass_ConvertTemp_Request._TYPE_SUPPORT is None:
                _convert_temp.Metaclass_ConvertTemp_Request.__import_type_support__()
            if _convert_temp.Metaclass_ConvertTemp_Response._TYPE_SUPPORT is None:
                _convert_temp.Metaclass_ConvertTemp_Response.__import_type_support__()


class ConvertTemp(metaclass=Metaclass_ConvertTemp):
    from service_temp.srv._convert_temp import ConvertTemp_Request as Request
    from service_temp.srv._convert_temp import ConvertTemp_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
