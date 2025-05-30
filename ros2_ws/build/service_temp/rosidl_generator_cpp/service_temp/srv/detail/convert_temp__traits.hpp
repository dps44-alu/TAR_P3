// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from service_temp:srv/ConvertTemp.idl
// generated code does not contain a copyright notice

#ifndef SERVICE_TEMP__SRV__DETAIL__CONVERT_TEMP__TRAITS_HPP_
#define SERVICE_TEMP__SRV__DETAIL__CONVERT_TEMP__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "service_temp/srv/detail/convert_temp__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace service_temp
{

namespace srv
{

inline void to_flow_style_yaml(
  const ConvertTemp_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: input_temp
  {
    out << "input_temp: ";
    rosidl_generator_traits::value_to_yaml(msg.input_temp, out);
    out << ", ";
  }

  // member: conversion_type
  {
    out << "conversion_type: ";
    rosidl_generator_traits::value_to_yaml(msg.conversion_type, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ConvertTemp_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: input_temp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "input_temp: ";
    rosidl_generator_traits::value_to_yaml(msg.input_temp, out);
    out << "\n";
  }

  // member: conversion_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "conversion_type: ";
    rosidl_generator_traits::value_to_yaml(msg.conversion_type, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ConvertTemp_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace service_temp

namespace rosidl_generator_traits
{

[[deprecated("use service_temp::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const service_temp::srv::ConvertTemp_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  service_temp::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use service_temp::srv::to_yaml() instead")]]
inline std::string to_yaml(const service_temp::srv::ConvertTemp_Request & msg)
{
  return service_temp::srv::to_yaml(msg);
}

template<>
inline const char * data_type<service_temp::srv::ConvertTemp_Request>()
{
  return "service_temp::srv::ConvertTemp_Request";
}

template<>
inline const char * name<service_temp::srv::ConvertTemp_Request>()
{
  return "service_temp/srv/ConvertTemp_Request";
}

template<>
struct has_fixed_size<service_temp::srv::ConvertTemp_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<service_temp::srv::ConvertTemp_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<service_temp::srv::ConvertTemp_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace service_temp
{

namespace srv
{

inline void to_flow_style_yaml(
  const ConvertTemp_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: converted_temp
  {
    out << "converted_temp: ";
    rosidl_generator_traits::value_to_yaml(msg.converted_temp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ConvertTemp_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: converted_temp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "converted_temp: ";
    rosidl_generator_traits::value_to_yaml(msg.converted_temp, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ConvertTemp_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace service_temp

namespace rosidl_generator_traits
{

[[deprecated("use service_temp::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const service_temp::srv::ConvertTemp_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  service_temp::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use service_temp::srv::to_yaml() instead")]]
inline std::string to_yaml(const service_temp::srv::ConvertTemp_Response & msg)
{
  return service_temp::srv::to_yaml(msg);
}

template<>
inline const char * data_type<service_temp::srv::ConvertTemp_Response>()
{
  return "service_temp::srv::ConvertTemp_Response";
}

template<>
inline const char * name<service_temp::srv::ConvertTemp_Response>()
{
  return "service_temp/srv/ConvertTemp_Response";
}

template<>
struct has_fixed_size<service_temp::srv::ConvertTemp_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<service_temp::srv::ConvertTemp_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<service_temp::srv::ConvertTemp_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<service_temp::srv::ConvertTemp>()
{
  return "service_temp::srv::ConvertTemp";
}

template<>
inline const char * name<service_temp::srv::ConvertTemp>()
{
  return "service_temp/srv/ConvertTemp";
}

template<>
struct has_fixed_size<service_temp::srv::ConvertTemp>
  : std::integral_constant<
    bool,
    has_fixed_size<service_temp::srv::ConvertTemp_Request>::value &&
    has_fixed_size<service_temp::srv::ConvertTemp_Response>::value
  >
{
};

template<>
struct has_bounded_size<service_temp::srv::ConvertTemp>
  : std::integral_constant<
    bool,
    has_bounded_size<service_temp::srv::ConvertTemp_Request>::value &&
    has_bounded_size<service_temp::srv::ConvertTemp_Response>::value
  >
{
};

template<>
struct is_service<service_temp::srv::ConvertTemp>
  : std::true_type
{
};

template<>
struct is_service_request<service_temp::srv::ConvertTemp_Request>
  : std::true_type
{
};

template<>
struct is_service_response<service_temp::srv::ConvertTemp_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SERVICE_TEMP__SRV__DETAIL__CONVERT_TEMP__TRAITS_HPP_
