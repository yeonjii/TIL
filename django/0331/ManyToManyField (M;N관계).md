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


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

3개의 테이블이 생긴다.

![image-20210331102005825](https://user-images.githubusercontent.com/77573938/113165699-1a047880-927d-11eb-831b-17ce9dfaf9bf.png)

![3](https://user-images.githubusercontent.com/77573938/113165688-17098800-927d-11eb-91f7-8d9f9ace0527.png)

<br><br>

## ManyToManyField 활용

> Doctor와 Patient의 관계를 맺기 위한 정보(서로의 id값 저장)만 필요한 경우 ManyToManyField 정의만 해주면 된다.
>
> ManyToManyField를 사용하면 여러 유용한 메서드를 활용할 수 있다.

https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-many-relationships

⭐ **다만, 추가적인 데이터를 넣고 싶으면 중개테이블을 직접 작성해야한다.** -> _through 명령어 추가해야함_ 

 ManyToManyField는 참조하는 외래키에 대한 필드만 생성해준다.

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor)
    
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

<br>

### Related manager

> 1: N 또는 M:N 관련 컨텍스트에서 사용되는 매니저

- 같은 이름의 매서드여도 각 관계(1: N, M:N)에 따라 다르게 동작
- 1:N 에서는 target 모델 객체만 사용 가능
- M:N에서는 관련된 두 객체에서 모두 사용 가능
- methods : `add()`, `create()`, `remove()`, `clear()`, `set()`

<br>

ManyToMAnyField는 관계 추가, 삭제 등을 위한 유용한 메서드 들이 많다.

```python
patient.doctors.add(doctor1)  # 관계 추가 (바로 DB에 저장됨)
patient.doctors.remove(doctor1)  # 관계 삭제
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

![5](https://user-images.githubusercontent.com/77573938/113165695-196be200-927d-11eb-8707-19ce6c41b0da.png)

<br><br>

## related_name 옵션

> - 역참조시 모델매니저의 이름을 바꾸는 외래키 인자
>- target model이 source model(관계 필드를 가진 모델)을 참조할 때 사용할 manager name
> - patient가 doctors로 접근하는 것처럼, doctor가 patient를 역참조할 때 patient_set이 아닌 patients와 같은 이름으로 접근할 수 있다.

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

![6](https://user-images.githubusercontent.com/77573938/113165697-196be200-927d-11eb-804e-bfd488fb639c.png)