# M : N (다대다 관계)

> 실제 DB 관점에서의 본질은 1:N 관계를 활용하여 M:N 관계를 표현한 것이다.
>
> 하지만 우리는 장고에서 제공하는 기능을 활용하여 M:N 관계를 조금 더 유용하게, 입맛대로 가공해서 활용할 수 있다.

<br>

💡 Example) **병원에 내원하는 환자와 의사의 예약 시스템 구상**

- 의사 & 환자 간의 진료시스템 -> 의사 & 환자 2개의 모델 필요

- 그러나, 일반적인 1:N 관계의 경우, Doctor와 Patient 모델 둘 만으로는 부족.
  
  ex. 한명의 환자가 2명의 의사한테 진료를 받거나, 예약 의사를 변경할 경우

**=> Doctor, Patient의 pk값을 가지고 있는 중개테이블(중개모델) 만들기 !**

<br><br>

## 1:N 관계를 갖는 중개 테이블

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 중개 테이블 (외래키 2개)
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

3개의 테이블이 생긴다.

![image-20210331102005825](https://user-images.githubusercontent.com/77573938/113165699-1a047880-927d-11eb-831b-17ce9dfaf9bf.png)

<img src="https://user-images.githubusercontent.com/77573938/113165688-17098800-927d-11eb-91f7-8d9f9ace0527.png" alt="3" style="zoom:25%;" />



```shell
In [1]: doctor1 = Doctor.objects.create(name='justin')

In [2]: patient1 = Patient.objects.create(name='tony')

In [3]: Reservation.objects.create(doctor=doctor1, patient=patient1)
Out[3]: <Reservation: 1번 의사의 1번 환자>

In [4]: patient2 = Patient.objects.create(name='harry')

In [5]: Reservation.objects.create(doctor=doctor1, patient=patient2)
Out[5]: <Reservation: 1번 의사의 2번 환자>

In [6]: doctor1.reservation_set.all()  # 역참조 - 의사입장
Out[6]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>

In [7]: patient1.reservation_set.all()  # 역참조 - 환자입장
Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>


# 쿼리셋 -> 반복문 출력 가능
In [8]: for reservation in doctor1.reservation_set.all():
    ...:     print(reservation.patient.name)
    ...: 
tony
harry
```

<br><br>

## ManyToManyField

> - M:N 관계를 지원해주는 장고 제공 field (many to many field)
>
> Doctor와 Patient의 관계를 맺기 위한 정보(서로의 id값 저장)만 필요한 경우 ManyToManyField 정의만 해주면 된다.
>
> ManyToManyField를 사용하면 여러 유용한 메서드를 활용할 수 있다.

https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-many-relationships

⭐ **다만, 추가적인 데이터를 넣고 싶으면 중개테이블을 직접 작성해야한다. -> _through 명령어 추가해야함_** 

 ManyToManyField는 참조하는 외래키에 대한 필드만 생성해준다.

<br>

ManyToManyField는 Doctor든 Patient든 둘 중 하나에 작성하면 된다.

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor)  # 참조하는 모델의 복수형으로 작성
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
# 
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

django가 `앱네임_모델명_ManyToManyField명` 의 중개테이블을 자동으로 만들어준다.

![4](https://user-images.githubusercontent.com/77573938/113165694-18d34b80-927d-11eb-881f-530bc94ed3f2.png)



### Related manager

> 1: N 또는 M:N 관련 컨텍스트에서 사용되는 매니저

- 같은 이름의 매서드여도 각 관계(1: N, M:N)에 따라 다르게 동작

- 1:N 에서는 target 모델 객체만 사용 가능

  _cf )_ 

  - source model (instance) : 관계 필드를 가진 모델
  - target model (instance) : source model이 관계 필드를 통해 참조하는 모델
  - ex. Article: target model - Commet: source model

- M:N에서는 관련된 두 객체에서 모두 사용 가능

- methods : `add()`, `create()`, `remove()`, `clear()`, `set()`

<br>

ManyToManyField는 관계 추가, 삭제 등을 위한 유용한 메서드 들이 많다.

```python
patient1.doctors.add(doctor1)  # 관계 추가 (바로 DB에 저장됨)
patient1.doctors.remove(doctor1)  # 관계 삭제
```

<br>

이제 중개테이블(Reservation)을 거치지 않고 Doctor, Patient 바로바로 참조 가능하다.

```shell
In [1]: doctor1 = Doctor.objects.create(name='justin')

In [2]: doctor2 = Doctor.objects.create(name='eric')

In [3]: patient1 = Patient.objects.create(name='tony')

In [4]: patient2 = Patient.objects.create(name='harry')

In [5]: patient1.doctors.add(doctor1)

In [6]: patient1.doctors.all()  # 환자 입장에서 의사 추가
Out[6]: <QuerySet [<Doctor: 1번 의사 justin>]>

In [7]: doctor1.patient_set.all()  # 역참조: 자신을 참조하는 테이블을 참조하는거. 1에서 N을 참조하는게 아님!
Out[8]: <QuerySet [<Patient: 1번 환자 tony>]>

In [9]: doctor1.patient_set.add(patient2)  # 의사 입장에서 환자 추가

In [10]: doctor1.patient_set.remove(patient1)  # 의사가 예약 취소

In [11]: patient2.doctors.remove(doctor1)  # 환자가 예약 취소
```

<br><br>

## through 옵션

> 추가적인 데이터가 필요한 경우 중개 테이블을 생성하고 through 옵션으로 연결한다.

나중에 추가적인 데이터(필드)가 필요할 수 있는 경우, 이렇게 모델링 하는게 확장성이 더 좋다.

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

<img src="https://user-images.githubusercontent.com/77573938/113165695-196be200-927d-11eb-8707-19ce6c41b0da.png" alt="5" style="zoom:25%;" />

<br><br>

## related_name 옵션

> - 역참조시 모델매니저의 이름을 바꾸는 외래키 인자
>- target model이 source model(관계 필드를 가진 모델)을 참조할 때 사용할 manager name
> - patient가 doctors로 접근하는 것처럼, doctor가 patient를 역참조할 때 patient_set이 아닌 patients와 같은 이름으로 접근할 수 있다.

<br>

`patient_set`은 더이상 사용 불가. `patients`로 사용해야 한다.

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

<img src="https://user-images.githubusercontent.com/77573938/113165697-196be200-927d-11eb-804e-bfd488fb639c.png" alt="6" style="zoom:25%;" />