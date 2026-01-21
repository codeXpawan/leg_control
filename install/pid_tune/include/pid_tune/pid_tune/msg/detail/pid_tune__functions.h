// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from pid_tune:msg/PidTune.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "pid_tune/msg/pid_tune.h"


#ifndef PID_TUNE__MSG__DETAIL__PID_TUNE__FUNCTIONS_H_
#define PID_TUNE__MSG__DETAIL__PID_TUNE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_runtime_c/type_description/type_description__struct.h"
#include "rosidl_runtime_c/type_description/type_source__struct.h"
#include "rosidl_runtime_c/type_hash.h"
#include "rosidl_runtime_c/visibility_control.h"
#include "pid_tune/msg/rosidl_generator_c__visibility_control.h"

#include "pid_tune/msg/detail/pid_tune__struct.h"

/// Initialize msg/PidTune message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * pid_tune__msg__PidTune
 * )) before or use
 * pid_tune__msg__PidTune__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
bool
pid_tune__msg__PidTune__init(pid_tune__msg__PidTune * msg);

/// Finalize msg/PidTune message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
void
pid_tune__msg__PidTune__fini(pid_tune__msg__PidTune * msg);

/// Create msg/PidTune message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * pid_tune__msg__PidTune__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
pid_tune__msg__PidTune *
pid_tune__msg__PidTune__create(void);

/// Destroy msg/PidTune message.
/**
 * It calls
 * pid_tune__msg__PidTune__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
void
pid_tune__msg__PidTune__destroy(pid_tune__msg__PidTune * msg);

/// Check for msg/PidTune message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
bool
pid_tune__msg__PidTune__are_equal(const pid_tune__msg__PidTune * lhs, const pid_tune__msg__PidTune * rhs);

/// Copy a msg/PidTune message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
bool
pid_tune__msg__PidTune__copy(
  const pid_tune__msg__PidTune * input,
  pid_tune__msg__PidTune * output);

/// Retrieve pointer to the hash of the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
const rosidl_type_hash_t *
pid_tune__msg__PidTune__get_type_hash(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
const rosidl_runtime_c__type_description__TypeDescription *
pid_tune__msg__PidTune__get_type_description(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the single raw source text that defined this type.
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
const rosidl_runtime_c__type_description__TypeSource *
pid_tune__msg__PidTune__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the recursive raw sources that defined the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
const rosidl_runtime_c__type_description__TypeSource__Sequence *
pid_tune__msg__PidTune__get_type_description_sources(
  const rosidl_message_type_support_t * type_support);

/// Initialize array of msg/PidTune messages.
/**
 * It allocates the memory for the number of elements and calls
 * pid_tune__msg__PidTune__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
bool
pid_tune__msg__PidTune__Sequence__init(pid_tune__msg__PidTune__Sequence * array, size_t size);

/// Finalize array of msg/PidTune messages.
/**
 * It calls
 * pid_tune__msg__PidTune__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
void
pid_tune__msg__PidTune__Sequence__fini(pid_tune__msg__PidTune__Sequence * array);

/// Create array of msg/PidTune messages.
/**
 * It allocates the memory for the array and calls
 * pid_tune__msg__PidTune__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
pid_tune__msg__PidTune__Sequence *
pid_tune__msg__PidTune__Sequence__create(size_t size);

/// Destroy array of msg/PidTune messages.
/**
 * It calls
 * pid_tune__msg__PidTune__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
void
pid_tune__msg__PidTune__Sequence__destroy(pid_tune__msg__PidTune__Sequence * array);

/// Check for msg/PidTune message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
bool
pid_tune__msg__PidTune__Sequence__are_equal(const pid_tune__msg__PidTune__Sequence * lhs, const pid_tune__msg__PidTune__Sequence * rhs);

/// Copy an array of msg/PidTune messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pid_tune
bool
pid_tune__msg__PidTune__Sequence__copy(
  const pid_tune__msg__PidTune__Sequence * input,
  pid_tune__msg__PidTune__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // PID_TUNE__MSG__DETAIL__PID_TUNE__FUNCTIONS_H_
