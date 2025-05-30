// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from service_temp:srv/ConvertTemp.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "service_temp/srv/detail/convert_temp__rosidl_typesupport_introspection_c.h"
#include "service_temp/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "service_temp/srv/detail/convert_temp__functions.h"
#include "service_temp/srv/detail/convert_temp__struct.h"


// Include directives for member types
// Member `conversion_type`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  service_temp__srv__ConvertTemp_Request__init(message_memory);
}

void service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_fini_function(void * message_memory)
{
  service_temp__srv__ConvertTemp_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_member_array[2] = {
  {
    "input_temp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(service_temp__srv__ConvertTemp_Request, input_temp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "conversion_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(service_temp__srv__ConvertTemp_Request, conversion_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_members = {
  "service_temp__srv",  // message namespace
  "ConvertTemp_Request",  // message name
  2,  // number of fields
  sizeof(service_temp__srv__ConvertTemp_Request),
  service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_member_array,  // message members
  service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_type_support_handle = {
  0,
  &service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_temp
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp_Request)() {
  if (!service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_type_support_handle.typesupport_identifier) {
    service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &service_temp__srv__ConvertTemp_Request__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "service_temp/srv/detail/convert_temp__rosidl_typesupport_introspection_c.h"
// already included above
// #include "service_temp/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "service_temp/srv/detail/convert_temp__functions.h"
// already included above
// #include "service_temp/srv/detail/convert_temp__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  service_temp__srv__ConvertTemp_Response__init(message_memory);
}

void service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_fini_function(void * message_memory)
{
  service_temp__srv__ConvertTemp_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_member_array[1] = {
  {
    "converted_temp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(service_temp__srv__ConvertTemp_Response, converted_temp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_members = {
  "service_temp__srv",  // message namespace
  "ConvertTemp_Response",  // message name
  1,  // number of fields
  sizeof(service_temp__srv__ConvertTemp_Response),
  service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_member_array,  // message members
  service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_type_support_handle = {
  0,
  &service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_temp
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp_Response)() {
  if (!service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_type_support_handle.typesupport_identifier) {
    service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &service_temp__srv__ConvertTemp_Response__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "service_temp/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "service_temp/srv/detail/convert_temp__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_members = {
  "service_temp__srv",  // service namespace
  "ConvertTemp",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_Request_message_type_support_handle,
  NULL  // response message
  // service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_Response_message_type_support_handle
};

static rosidl_service_type_support_t service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_type_support_handle = {
  0,
  &service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_service_temp
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp)() {
  if (!service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_type_support_handle.typesupport_identifier) {
    service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_temp, srv, ConvertTemp_Response)()->data;
  }

  return &service_temp__srv__detail__convert_temp__rosidl_typesupport_introspection_c__ConvertTemp_service_type_support_handle;
}
