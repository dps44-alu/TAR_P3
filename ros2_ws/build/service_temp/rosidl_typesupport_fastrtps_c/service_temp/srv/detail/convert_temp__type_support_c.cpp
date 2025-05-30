// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from service_temp:srv/ConvertTemp.idl
// generated code does not contain a copyright notice
#include "service_temp/srv/detail/convert_temp__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "service_temp/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "service_temp/srv/detail/convert_temp__struct.h"
#include "service_temp/srv/detail/convert_temp__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // conversion_type
#include "rosidl_runtime_c/string_functions.h"  // conversion_type

// forward declare type support functions


using _ConvertTemp_Request__ros_msg_type = service_temp__srv__ConvertTemp_Request;

static bool _ConvertTemp_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ConvertTemp_Request__ros_msg_type * ros_message = static_cast<const _ConvertTemp_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: input_temp
  {
    cdr << ros_message->input_temp;
  }

  // Field name: conversion_type
  {
    const rosidl_runtime_c__String * str = &ros_message->conversion_type;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _ConvertTemp_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ConvertTemp_Request__ros_msg_type * ros_message = static_cast<_ConvertTemp_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: input_temp
  {
    cdr >> ros_message->input_temp;
  }

  // Field name: conversion_type
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->conversion_type.data) {
      rosidl_runtime_c__String__init(&ros_message->conversion_type);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->conversion_type,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'conversion_type'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_service_temp
size_t get_serialized_size_service_temp__srv__ConvertTemp_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ConvertTemp_Request__ros_msg_type * ros_message = static_cast<const _ConvertTemp_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name input_temp
  {
    size_t item_size = sizeof(ros_message->input_temp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name conversion_type
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->conversion_type.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _ConvertTemp_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_service_temp__srv__ConvertTemp_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_service_temp
size_t max_serialized_size_service_temp__srv__ConvertTemp_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: input_temp
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: conversion_type
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = service_temp__srv__ConvertTemp_Request;
    is_plain =
      (
      offsetof(DataType, conversion_type) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ConvertTemp_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_service_temp__srv__ConvertTemp_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ConvertTemp_Request = {
  "service_temp::srv",
  "ConvertTemp_Request",
  _ConvertTemp_Request__cdr_serialize,
  _ConvertTemp_Request__cdr_deserialize,
  _ConvertTemp_Request__get_serialized_size,
  _ConvertTemp_Request__max_serialized_size
};

static rosidl_message_type_support_t _ConvertTemp_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ConvertTemp_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, service_temp, srv, ConvertTemp_Request)() {
  return &_ConvertTemp_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "service_temp/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "service_temp/srv/detail/convert_temp__struct.h"
// already included above
// #include "service_temp/srv/detail/convert_temp__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _ConvertTemp_Response__ros_msg_type = service_temp__srv__ConvertTemp_Response;

static bool _ConvertTemp_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ConvertTemp_Response__ros_msg_type * ros_message = static_cast<const _ConvertTemp_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: converted_temp
  {
    cdr << ros_message->converted_temp;
  }

  return true;
}

static bool _ConvertTemp_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ConvertTemp_Response__ros_msg_type * ros_message = static_cast<_ConvertTemp_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: converted_temp
  {
    cdr >> ros_message->converted_temp;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_service_temp
size_t get_serialized_size_service_temp__srv__ConvertTemp_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ConvertTemp_Response__ros_msg_type * ros_message = static_cast<const _ConvertTemp_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name converted_temp
  {
    size_t item_size = sizeof(ros_message->converted_temp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ConvertTemp_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_service_temp__srv__ConvertTemp_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_service_temp
size_t max_serialized_size_service_temp__srv__ConvertTemp_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: converted_temp
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = service_temp__srv__ConvertTemp_Response;
    is_plain =
      (
      offsetof(DataType, converted_temp) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _ConvertTemp_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_service_temp__srv__ConvertTemp_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_ConvertTemp_Response = {
  "service_temp::srv",
  "ConvertTemp_Response",
  _ConvertTemp_Response__cdr_serialize,
  _ConvertTemp_Response__cdr_deserialize,
  _ConvertTemp_Response__get_serialized_size,
  _ConvertTemp_Response__max_serialized_size
};

static rosidl_message_type_support_t _ConvertTemp_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ConvertTemp_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, service_temp, srv, ConvertTemp_Response)() {
  return &_ConvertTemp_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "service_temp/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "service_temp/srv/convert_temp.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t ConvertTemp__callbacks = {
  "service_temp::srv",
  "ConvertTemp",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, service_temp, srv, ConvertTemp_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, service_temp, srv, ConvertTemp_Response)(),
};

static rosidl_service_type_support_t ConvertTemp__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &ConvertTemp__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, service_temp, srv, ConvertTemp)() {
  return &ConvertTemp__handle;
}

#if defined(__cplusplus)
}
#endif
