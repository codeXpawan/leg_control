// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from pid_tune:msg/PidTune.idl
// generated code does not contain a copyright notice
#include "pid_tune/msg/detail/pid_tune__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <cstddef>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "pid_tune/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "pid_tune/msg/detail/pid_tune__struct.h"
#include "pid_tune/msg/detail/pid_tune__functions.h"
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


// forward declare type support functions


using _PidTune__ros_msg_type = pid_tune__msg__PidTune;


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
bool cdr_serialize_pid_tune__msg__PidTune(
  const pid_tune__msg__PidTune * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: kp
  {
    cdr << ros_message->kp;
  }

  // Field name: ki
  {
    cdr << ros_message->ki;
  }

  // Field name: kd
  {
    cdr << ros_message->kd;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
bool cdr_deserialize_pid_tune__msg__PidTune(
  eprosima::fastcdr::Cdr & cdr,
  pid_tune__msg__PidTune * ros_message)
{
  // Field name: kp
  {
    cdr >> ros_message->kp;
  }

  // Field name: ki
  {
    cdr >> ros_message->ki;
  }

  // Field name: kd
  {
    cdr >> ros_message->kd;
  }

  return true;
}  // NOLINT(readability/fn_size)


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t get_serialized_size_pid_tune__msg__PidTune(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _PidTune__ros_msg_type * ros_message = static_cast<const _PidTune__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: kp
  {
    size_t item_size = sizeof(ros_message->kp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: ki
  {
    size_t item_size = sizeof(ros_message->ki);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: kd
  {
    size_t item_size = sizeof(ros_message->kd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t max_serialized_size_pid_tune__msg__PidTune(
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

  // Field name: kp
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: ki
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: kd
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
    using DataType = pid_tune__msg__PidTune;
    is_plain =
      (
      offsetof(DataType, kd) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
bool cdr_serialize_key_pid_tune__msg__PidTune(
  const pid_tune__msg__PidTune * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: kp
  {
    cdr << ros_message->kp;
  }

  // Field name: ki
  {
    cdr << ros_message->ki;
  }

  // Field name: kd
  {
    cdr << ros_message->kd;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t get_serialized_size_key_pid_tune__msg__PidTune(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _PidTune__ros_msg_type * ros_message = static_cast<const _PidTune__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;

  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: kp
  {
    size_t item_size = sizeof(ros_message->kp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: ki
  {
    size_t item_size = sizeof(ros_message->ki);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: kd
  {
    size_t item_size = sizeof(ros_message->kd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_pid_tune
size_t max_serialized_size_key_pid_tune__msg__PidTune(
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
  // Field name: kp
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: ki
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: kd
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
    using DataType = pid_tune__msg__PidTune;
    is_plain =
      (
      offsetof(DataType, kd) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}


static bool _PidTune__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const pid_tune__msg__PidTune * ros_message = static_cast<const pid_tune__msg__PidTune *>(untyped_ros_message);
  (void)ros_message;
  return cdr_serialize_pid_tune__msg__PidTune(ros_message, cdr);
}

static bool _PidTune__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  pid_tune__msg__PidTune * ros_message = static_cast<pid_tune__msg__PidTune *>(untyped_ros_message);
  (void)ros_message;
  return cdr_deserialize_pid_tune__msg__PidTune(cdr, ros_message);
}

static uint32_t _PidTune__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_pid_tune__msg__PidTune(
      untyped_ros_message, 0));
}

static size_t _PidTune__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_pid_tune__msg__PidTune(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_PidTune = {
  "pid_tune::msg",
  "PidTune",
  _PidTune__cdr_serialize,
  _PidTune__cdr_deserialize,
  _PidTune__get_serialized_size,
  _PidTune__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _PidTune__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_PidTune,
  get_message_typesupport_handle_function,
  &pid_tune__msg__PidTune__get_type_hash,
  &pid_tune__msg__PidTune__get_type_description,
  &pid_tune__msg__PidTune__get_type_description_sources,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, pid_tune, msg, PidTune)() {
  return &_PidTune__type_support;
}

#if defined(__cplusplus)
}
#endif
