
(cl:in-package :asdf)

(defsystem "p2pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "MiMensaje" :depends-on ("_package_MiMensaje"))
    (:file "_package_MiMensaje" :depends-on ("_package"))
  ))